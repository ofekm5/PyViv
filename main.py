import os
import subprocess
import argparse
from datetime import datetime

# TODO! make from this script a local pip package(turn this folder into src)


# Example usage: python main.py "./entityX/entityX.vhd" --vivado "C:/Xilinx/Vivado/2024.1/bin/vivado.bat"

def run_vivado(vhdl_file, ip_dir, vivado_path):
    curr_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    journal_file = f"vivado_session_{curr_datetime}.jou"
    log_file = f"vivado_session_{curr_datetime}.log"
    tcl_script = os.path.join(os.path.dirname(__file__), "wrap_vhdl_as_ip.tcl")
    
    if not os.path.isfile(tcl_script):
        print(f"\033[31mERROR: TCL script '{tcl_script}' not found.\033[0m")
        return

    command = [
        vivado_path, "-mode", "batch",
        "-source", tcl_script,
        "-journal", journal_file,  
        "-log", log_file,          
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
    parser.add_argument("--vivado", default="vivado", help="Path to the Vivado executable (default: 'vivado').")

    args = parser.parse_args()

    # Validate inputs
    if not os.path.isfile(args.vhdl_file):
        print(f"\033[31mERROR: VHDL file '{args.vhdl_file}' not found.\033[0m")
        return

    # Infer IP package directory from the VHDL file path
    vhdl_dir = os.path.dirname(args.vhdl_file)
    ip_dir = os.path.join(vhdl_dir, "ip_package")

    if not os.path.isdir(ip_dir):
        print(f"\033[33mINFO: Directory '{ip_dir}' does not exist. Creating it...\033[0m")
        os.makedirs(ip_dir)

    # Run Vivado
    run_vivado(args.vhdl_file, ip_dir, args.vivado)

if __name__ == "__main__":
    main()
