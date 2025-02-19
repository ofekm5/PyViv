# Argument handling
if { [llength $argv] != 1 } {
    puts "ERROR: Expected 1 argument: <project_repo_path>"
    exit 1
}

set project_repo_path [lindex $argv 0]
set project_name [file tail $project_repo_path]
set project_file_path "$project_repo_path/$project_name.xpr"

# Validate that the project exists
if { ![file exists $project_file_path] } {
    puts "ERROR: Project file $project_file_path does not exist."
    exit 1
}

# Open the Vivado project
puts "INFO: Opening project $project_file_path"
open_project $project_file_path

# Ensure block design is up-to-date
puts "INFO: Updating compile order"
update_compile_order -fileset sources_1

# Synthesize and generate bitstream
puts "INFO: Running synthesis"
synth_design
puts "INFO: Writing checkpoint"
write_checkpoint -force "$project_repo_path/design_checkpoint.dcp"

# Run implementation
puts "INFO: Running implementation"
open_run impl_1
puts "INFO: Writing bitstream"
write_bitstream -force "$project_repo_path/design.bit"

# Export hardware with bitstream
set xsa_file "$project_repo_path/${project_name}_hw.xsa"
puts "INFO: Exporting hardware to $xsa_file"
export_hardware -bitstream "$project_repo_path/design.bit" -file $xsa_file

# Close project
puts "INFO: Closing project"
close_project
puts "INFO: XSA export completed successfully"

quit
