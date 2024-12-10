import os
import subprocess
import re
import argparse

# TODO! 
# make from this script a local pip package(turn this folder into src)
# route all logs and journals into a file that is emptied



# Example usage:
# python main.py ./entityX/entityX.vhd ./entityX/ip_package
# When Vivaldo is not in the PATH:
# python main.py "./entityX/entityX.vhd" "./entityX/ip_package" --vivado "C:/Xilinx/Vivado/2024.1/bin/vivado.bat"
# python main.py "C:\Users\avita\Documents\Template\Template.srcs\sources_1\Comp\Comp.vhd" "C:\Users\avita\Documents\Template\Template.srcs\sources_1\Comp\ip_package" --vivado "C:/Xilinx/Vivado/2024.1/bin/vivado.bat"

def run_vivado(vhdl_file, ip_dir, vivado_path):
    """
    Runs Vivado with the provided TCL script and arguments.
    
    Args:
        vhdl_file (str): Path to the VHDL file.
        ip_dir (str): Directory for the generated IP.
        vivado_path (str): Path to the Vivado executable.
    """
    tcl_script = os.path.join(os.path.dirname(__file__), "wrap_vhdl_as_ip.tcl")
    
    if not os.path.isfile(tcl_script):
        print(f"\033[31mERROR: TCL script '{tcl_script}' not found.\033[0m")
        return

    command = [
        vivado_path, "-mode", "batch",
        "-source", tcl_script,
        "-tclargs", vhdl_file, ip_dir
    ]

    print(f"\n\033[34m{'-' * 50}\033[0m")
    print(f"\033[34mRunning Vivado: {' '.join(command)}\033[0m")
    print(f"\033[34m{'-' * 50}\033[0m\n")

    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    # Process output line by line
    for line in process.stdout:
        format_vivado_output(line)

    # Process any errors
    for line in process.stderr:
        format_vivado_output(line)

    # Wait for process to complete
    process.wait()
    if process.returncode != 0:
        print(f"\033[31mError: Vivado exited with code {process.returncode}\033[0m")
    else:
        print("\033[32mVivado completed successfully.\033[0m")

def format_vivado_output(line):
    """Formats Vivado output with regex for better readability."""
    # Skip lines starting with #
    if line.strip().startswith("#"):
        return
    
    if "ERROR" in line:
        print(f"\033[31m{line.strip()}\033[0m")  # Red for errors
    elif "WARNING" in line:
        print(f"\033[33m{line.strip()}\033[0m")  # Yellow for warnings
    elif "INFO" in line:
        print(f"\033[32m{line.strip()}\033[0m")  # Green for info
    else:
        print(f"\033[34m{line.strip()}\033[0m")  # Blue for other output



def main():
    parser = argparse.ArgumentParser(description="VHDL IP Wrapper Tool")
    parser.add_argument("vhdl_file", help="Path to the VHDL file.")
    parser.add_argument("ip_dir", help="Output directory for the IP package.")
    parser.add_argument("--vivado", default="vivado", help="Path to the Vivado executable (default: 'vivado').")

    args = parser.parse_args()

    # Validate inputs
    if not os.path.isfile(args.vhdl_file):
        print(f"\033[31mERROR: VHDL file '{args.vhdl_file}' not found.\033[0m")
        return
    if not os.path.isdir(args.ip_dir):
        print(f"\033[33mINFO: Directory '{args.ip_dir}' does not exist. Creating it...\033[0m")
        os.makedirs(args.ip_dir)

    # Run Vivado
    run_vivado(args.vhdl_file, args.ip_dir, args.vivado)

if __name__ == "__main__":
    main()
