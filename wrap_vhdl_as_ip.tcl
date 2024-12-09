# Input arguments
if {[llength $::argv] < 2} {
    puts "ERROR: Please provide the VHDL file and output IP directory as arguments."
    puts "Usage: vivado -mode batch -source wrap_vhdl_as_ip.tcl -tclargs <vhdl_file> <output_dir>"
    exit 1
}

# Arguments: VHDL file and IP output directory
set vhdl_file [lindex $::argv 0]
set ip_dir [lindex $::argv 1]

# Normalize paths
set vhdl_file [string map {"\\" "/"} $vhdl_file]
set ip_dir [string map {"\\" "/"} $ip_dir]

# Validate input paths
if {![file exists $vhdl_file]} {
    puts "ERROR: VHDL file $vhdl_file does not exist."
    exit 1
}
if {![file isdirectory $ip_dir]} {
    puts "ERROR: Directory $ip_dir does not exist. Creating it..."
    file mkdir $ip_dir
}

puts "VHDL File: $vhdl_file"
puts "IP Directory: $ip_dir"

# Create a temporary project
puts "Creating temporary project..."
create_project temp_project ./temp_project -part xczu7ev-ffvc1156-2-e -force

# Add the VHDL file to the project
puts "Adding VHDL file to the project..."
if {[llength [get_files -quiet $vhdl_file]] == 0} {
    add_files $vhdl_file
    puts "INFO: File $vhdl_file added to the project."
} else {
    puts "INFO: File $vhdl_file already exists in the project, skipping."
}

# Set the top module name
set top_module [file tail $vhdl_file]
set top_module [file rootname $top_module]
puts "Setting top module to: $top_module"
set_property top $top_module [current_fileset]

# Auto-detect the FPGA family
puts "Detecting FPGA family..."
set device [get_property PART [current_project]]
set family [get_property FAMILY [get_parts -name $device]]
if {$family eq ""} {
    puts "WARNING: Could not detect the device family. Defaulting to 'zynquplus'."
    set family "zynquplus"
}
puts "Detected FPGA family: $family"

# Open the IP packaging interface
puts "Starting IP packaging process..."
ipx::package_project -root_dir $ip_dir -vendor user.org -library user_lib -taxonomy /UserIP -import_files

# Compatibility settings
puts "Setting compatibility options..."
ipx::edit_core_property compat_ipi 1
ipx::edit_core_property compatible_families "{$family}"
ipx::edit_core_property compatible_simulators "{Vivado Simulator}"

# Update ports and interfaces(applying port modifications in the IP)
puts "Updating ports and interfaces..."
ipx::update_ports

# Set interface attributes for clock ports
puts "Configuring clock ports..."
set clk_ports [get_ports -regexp .*clk.*]
foreach port $clk_ports {
    set_property port_intf external_clk $port
    puts "INFO: Setting interface for clock port $port"
}

# Set interface attributes for reset ports
puts "Configuring reset ports..."
set reset_ports [get_ports -regexp .*reset.*]
foreach port $reset_ports {
    set_property port_intf external_reset $port
    puts "INFO: Setting interface for reset port $port"
}

# Save the IP package
puts "Saving the IP package..."
ipx::save_core_source
puts "INFO: IP package saved successfully in $ip_dir"

# Clean up temporary project
puts "Cleaning up temporary project..."
close_project
file delete -force ./temp_project

puts "Done! IP packaged in $ip_dir"
