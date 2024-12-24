import os
import subprocess
import argparse

def run_tcl_script(tcl_script, vivado_path, args):
    """Runs a Vivado TCL script with the provided arguments."""
    if not os.path.isfile(tcl_script):
        print(f"\033[31mERROR: TCL script '{tcl_script}' not found.\033[0m")
        return

    command = [
        vivado_path, "-mode", "batch",
        "-source", tcl_script
    ] + args

    print(f"\n\033[34m{'-' * 50}\033[0m")
    print(f"\033[34mRunning Vivado: {' '.join(command)}\033[0m")
    print(f"\033[34m{'-' * 50}\033[0m\n")

    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    for line in process.stdout:
        format_vivado_output(line)

    for line in process.stderr:
        format_vivado_output(line)

    process.wait()
    if process.returncode != 0:
        print(f"\033[31mError: Vivado exited with code {process.returncode}\033[0m")
    else:
        print("\033[32mVivado completed successfully.\033[0m")


def format_vivado_output(line):
    """Formats Vivado output with regex for better readability."""
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


def buildArguments(args):
    tcl_args = []
    if args.operation in ["add_file", "check_syntax"]:
        if not args.file:
            print(f"\033[31mERROR: '--file' argument is required for '{args.operation}'.\033[0m")
            return
        
        tcl_args.append(args.file)

    return tcl_args


def main():
    parser = argparse.ArgumentParser(description="PyViv: A Vivado Management Tool")
    parser.add_argument("operation", choices=["add_file", "check_syntax", "create_wrapper"],
                        help="Operation to perform (e.g., add_file, check_syntax, create_wrapper).")
    parser.add_argument("--vivado", default="vivado", help="Path to the Vivado executable (default: 'vivado').")
    parser.add_argument("--file", help="Path to the VHDL file (for add_file or check_syntax operations).")

    args = parser.parse_args()

    # Map operations to their respective TCL scripts
    tcl_scripts = {
        "add_file": "scripts/add_remove_files.tcl",
        "check_syntax": "scripts/check_srcs_syntax.tcl",
        "create_wrapper": "scripts/create_vhdl_in_project.tcl"
    }

    tcl_script = tcl_scripts.get(args.operation)
    if not tcl_script:
        print(f"\033[31mERROR: Unsupported operation '{args.operation}'.\033[0m")
        return

    # Build arguments for the TCL script
    tcl_args = buildArguments(args)

    run_tcl_script(tcl_script, args.vivado, tcl_args)


if __name__ == "__main__":
    main()
