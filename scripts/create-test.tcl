# Argument handling
if { [llength $argv] != 2 } {
    puts "ERROR: Expected 2 arguments: <testbench_name> <project_repo_path>"
    exit 1
}

set testbench_name [lindex $argv 0]
set project_repo_path [lindex $argv 1]

# Get the project name from the project repository path
set project_name [file tail $project_repo_path]

# Construct paths
set testbench_folder_path "$project_repo_path/$project_name.srcs/sim_1/$testbench_name"
set testbench_file_path "$testbench_folder_path/$testbench_name.vhd"
set project_file_path "$project_repo_path/$project_name.xpr"

# Open the Vivado project
if { [file exists $project_file_path] } {
    open_project $project_file_path
} else {
    puts "ERROR: Project file $project_file_path does not exist."
    exit 1
}

# Create folder if it doesn't exist
if { ![file isdirectory $testbench_folder_path] } {
    puts "INFO: Creating directory $testbench_folder_path"
    file mkdir $testbench_folder_path
} else {
    puts "INFO: Directory $testbench_folder_path already exists"
}

# Define the VHDL testbench template
set tb_template {
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity TESTBENCH_NAME is
end TESTBENCH_NAME;

architecture Behavioral of TESTBENCH_NAME is
  signal clk : std_logic := '0';
  signal reset : std_logic := '1';
  signal din : std_logic_vector(7 downto 0) := (others => '0');
  signal dout : std_logic_vector(7 downto 0);

  constant clk_period : time := 10 ns;


begin
  uut: entity work.ENTITY_WRAPPER
    port map (
      clk => clk,
      reset => reset,
      din => din,
      dout => dout
    );

  clk_process: process
  begin
    clk <= '0';
    wait for 10 ns;
    clk <= '1';
    wait for 10 ns;
  end process;
  
  stimulus_process: process
  begin
  -- Apply reset (active low)
    reset <= '0';
    wait for 20 ns; -- Wait for reset to propagate
    reset <= '1';
    wait for 10 ns;
    en <= '1';

    -- Test case 1
    din <= "00000001"; 
    wait for clk_period;
    assert dout = "00000001" report "Test 1 failed" severity error;

    -- End simulation
    wait for 50 ns;
    report "Simulation finished successfully" severity note;
    assert false report "End of simulation" severity failure;
  end process;
end Behavioral;
}

# Write the VHDL testbench to the file
if { [file exists $testbench_file_path] } {
    puts "WARNING: Testbench file $testbench_file_path already exists. Overwriting."
} else {
    puts "INFO: Creating new testbench file $testbench_file_path"
}
set file_id [open $testbench_file_path w]
puts $file_id $tb_template
close $file_id

# Add the file to the simulation set and update the compile order
puts "INFO: Adding $testbench_file_path to the simulation fileset"
add_files -fileset sim_1 $testbench_file_path
update_compile_order -fileset sim_1

# Save and close project
puts "INFO: Testbench $testbench_name added successfully."
close_project
quit