# Argument handling
if { [llength $argv] != 2 } {
    puts "ERROR: Expected 2 arguments: <entity_name> <project_repo_path>"
    exit 1
}

set entity_name [lindex $argv 0]
set project_repo_path [lindex $argv 1]

# Get the project name from the project repository path
set project_name [file tail $project_repo_path]

# Construct paths
set entity_folder_path "$project_repo_path/$project_name.srcs/sources_1/$entity_name"
set entity_file_path "$entity_folder_path/$entity_name.vhd"
set project_file_path "$project_repo_path/$project_name.xpr"

# Open the Vivado project
if { [file exists $project_file_path] } {
    open_project $project_file_path
} else {
    puts "ERROR: Project file $project_file_path does not exist."
    exit 1
}

# Create folder if it doesn't exist
if { ![file isdirectory $entity_folder_path] } {
    puts "INFO: Creating directory $entity_folder_path"
    file mkdir $entity_folder_path
} else {
    puts "INFO: Directory $entity_folder_path already exists"
}

# Define the VHDL template
set vhdl_template {
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity ENTITY_NAME is
  Port (
    clk : in std_logic;
    reset : in std_logic;
    din : in std_logic_vector(7 downto 0);
    dout : out std_logic_vector(7 downto 0)
  );
end ENTITY_NAME;

architecture Behavioral of ENTITY_NAME is
begin
  process(clk)
  begin
    if rising_edge(clk) then
      if reset = '0' then
        dout <= (others => '0');
      else
        dout <= din;
      end if;
    end if;
  end process;
end Behavioral;
}

# Write the VHDL template to the file
if { [file exists $entity_file_path] } {
    puts "WARNING: Entity file $entity_file_path already exists. Overwriting."
} else {
    puts "INFO: Creating new entity file $entity_file_path"
}
set file_id [open $entity_file_path w]
puts $file_id $vhdl_template
close $file_id

puts "INFO: Adding $entity_file_path to the project"
add_files $entity_file_path

update_compile_order -fileset sources_1

close_project
quit
