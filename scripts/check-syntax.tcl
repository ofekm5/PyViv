# Argument handling
if { [llength $argv] != 1 } {
    puts "ERROR: Expected 1 argument: <project_repo_path>"
    exit 1
}

set project_repo_path [lindex $argv 0]

# Get the project name from the project repository path
set project_name [file tail $project_repo_path]
set project_file_path "$project_repo_path/$project_name.xpr"

# Open the Vivado project
if { [file exists $project_file_path] } {
    open_project $project_file_path
} else {
    puts "ERROR: Project file $project_file_path does not exist."
    exit 1
}

# Log start time
set start_time [clock seconds]
puts "INFO: Starting syntax check for fileset 'sources_1' at [clock format $start_time -format {%Y-%m-%d %H:%M:%S}]"

# Perform syntax check
set result [catch {check_syntax -fileset sources_1} errmsg]

if {$result == 0} {
    puts "INFO: Syntax check completed successfully."
} else {
    puts "ERROR: Syntax check failed. Details: $errmsg"
    exit 1
}

# Log end time
set end_time [clock seconds]
puts "INFO: Syntax check completed at [clock format $end_time -format {%Y-%m-%d %H:%M:%S}]. Duration: [expr $end_time - $start_time] seconds."

# Close the project
close_project
quit
