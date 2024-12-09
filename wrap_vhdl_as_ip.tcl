# Input arguments
if {[llength $::argv] < 2} {
    puts "ERROR: Please provide the VHDL file and output IP directory as arguments."
    puts "INFO: Usage: vivado -mode batch -source wrap_vhdl_as_ip.tcl -tclargs <vhdl_file> <output_dir>"
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
    puts "INFO: Directory $ip_dir does not exist. Creating it..."
    file mkdir $ip_dir
}

puts "INFO: VHDL File: $vhdl_file"
puts "INFO: IP Directory: $ip_dir"

# Static FPGA configuration
set static_part "xczu7ev-ffvc1156-2-e"  ;# Replace with your specific part
set static_family "zynquplus"           ;# Replace with your specific family

# Create a temporary project
puts "INFO: Creating temporary project..."
create_project temp_project ./temp_project -part $static_part -force

# Main processing with try-catch-finally
try {
    # Add the VHDL file to the project
    puts "INFO: Adding VHDL file to the project..."
    if {[llength [get_files -quiet $vhdl_file]] == 0} {
        add_files $vhdl_file
        puts "INFO: File $vhdl_file added to the project."
    } else {
        puts "INFO: File $vhdl_file already exists in the project, skipping."
    }

    # Set the top module name
    set top_module [file tail $vhdl_file]
    set top_module [file rootname $top_module]
    puts "INFO: Setting top module to: $top_module"
    set_property top $top_module [current_fileset]

    # Start IP packaging
    puts "INFO: Starting IP packaging process..."
    ipx::package_project -root_dir $ip_dir -vendor user.org -library user_lib -taxonomy /UserIP -import_files

    # Edit IP properties
    puts "INFO: Setting compatibility options..."
    ipx::edit_ip_in_project -name "ip_edit_project" -directory $ip_dir -force
    ipx::set_property compat_ipi true [ipx::current_core]
    ipx::set_property compatible_families "$static_family" [ipx::current_core]
    ipx::set_property compatible_simulators "Vivado Simulator" [ipx::current_core]

    # Update ports and interfaces
    puts "INFO: Updating ports and interfaces..."
    ipx::update_ports

    # Set interface attributes for clock ports
    puts "INFO: Configuring clock ports..."
    set clk_ports [get_ports -regexp .*clk.*]
    foreach port $clk_ports {
        set_property port_intf external_clk $port
        puts "INFO: Setting interface for clock port $port"
    }

    # Set interface attributes for reset ports
    puts "INFO: Configuring reset ports..."
    set reset_ports [get_ports -regexp .*reset.*]
    foreach port $reset_ports {
        set_property port_intf external_reset $port
        puts "INFO: Setting interface for reset port $port"
    }

    # Save the IP package
    puts "INFO: Saving the IP package..."
    ipx::save_core [ipx::current_core]
    puts "INFO: IP package saved successfully in $ip_dir"
} on error {errMsg} {
    puts "ERROR: An error occurred: $errMsg"
} finally {
    # Clean up temporary project
    puts "INFO: Cleaning up temporary project..."
    close_project
    file delete -force ./temp_project
}
