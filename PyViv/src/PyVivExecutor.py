import os
import subprocess

class PyVivExecutor:
    def __init__(self):
        pass

    def run_tcl_script(self, operation, vivado_path, tcl_args):
        """Runs a Vivado TCL script with the provided arguments."""
        tcl_script = f"../scripts/{operation}.tcl"

        if not os.path.isfile(tcl_script):
            print(f"\033[31mERROR: TCL script '{tcl_script}' not found.\033[0m")
            exit(1)

        command = [
            vivado_path, "-mode", "batch",
            "-source", tcl_script
        ] + tcl_args

        print(f"\n\033[34m{'-' * 50}\033[0m")
        print(f"\033[34mRunning Vivado: {' '.join(command)}\033[0m")
        print(f"\033[34m{'-' * 50}\033[0m\n")

        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        for line in process.stdout:
            self.__format_vivado_output(line)

        for line in process.stderr:
            self.__format_vivado_output(line)

        process.wait()
        if process.returncode != 0:
            print(f"\033[31mError: Vivado exited with code {process.returncode}\033[0m")
            exit(1)
        else:
            print("\033[32mVivado completed successfully.\033[0m")

    def __format_vivado_output(self, line):
        """Formats Vivado output with better readability."""
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