import argparse
import os

class PyVivConfig:
    def __init__(self):
        self.__pyviv_operations = ["create-entity", "create-test", "check-syntax", "add-path", "add-vivado", "export-xsa"]
        parser = argparse.ArgumentParser(description="PyViv: A VHDL Management Tool")
        parser.add_argument("operation", choices=self.__pyviv_operations, help="Operation to perform (e.g., create-entity, create-test, check-syntax, add-path).")
        parser.add_argument("--vivado", default="C:/Xilinx/Vivado/2024.2/bin/vivado.bat", help="Path to the Vivado executable (default: 'vivado').")
        parser.add_argument("--entity", help="Name of the VHDL entity (required for create-entity and create-test).")
        parser.add_argument("--path", default=os.getcwd(), help="Override the project repository path.")
        args = parser.parse_args()

        self.__vivado_path = args.vivado
        self.__operation = args.operation
        

        if args.operation == "add-path":
            if not args.path:
                print("\033[31mERROR: '--path' is required for 'add-path'.\033[0m")
                exit(1)
            self.__set_project_repo_path(args.path)
            return
        elif args.operation == "add-vivado":
            if not args.vivado:
                print("\033[31mERROR: '--vivado' is required for 'add-vivado'.\033[0m")
                exit(1)
            self.__set_vivado_path(args.vivado)
            return

        self.__project_repo = self.__get_project_repo_path(args.path)
        self.__vivado_path = self.__get_vivado_path(args.vivado)

        if args.operation in ["create-entity", "create-test"] and not args.entity:
            print(f"\033[31mERROR: '--entity' is required for '{args.operation}'.\033[0m")
            exit(1)

        self.__operation = args.operation
        self.__entity_name = args.entity
    
    def __get_vivado_path(self, path_override=None):
        config_file = os.path.expanduser("~/.pyviv_config")
        if path_override:
            return path_override

        return self.__get_config_value(config_file, "vivado_path", "ERROR: Vivado path not set. Use 'add-vivado' to set it.")

    def __get_project_repo_path(self, path_override=None):
        config_file = os.path.expanduser("~/.pyviv_config")
        if path_override:
            return path_override

        return self.__get_config_value(config_file, "project_repo_path", "ERROR: Project repository path not set. Use 'add-path' to set it.")

    def __get_config_value(self, config_file, key, error_message):
        """ Retrieves a specific configuration value by key. """
        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                for line in f:
                    k, v = line.strip().split("=", 1)
                    if k == key:
                        return v

        print(f"\033[31m{error_message}\033[0m")
        exit(1)

    def __set_vivado_path(self, path):
        config_file = os.path.expanduser("~/.pyviv_config")
        self.__update_config(config_file, "vivado_path", path)
        print(f"\033[32mINFO: Vivado path set to '{path}'.\033[0m")


    def __set_project_repo_path(self, path):
        config_file = os.path.expanduser("~/.pyviv_config")
        self.__update_config(config_file, "project_repo_path", path)
        print(f"\033[32mINFO: Project repository path set to '{path}'.\033[0m")

    def __update_config(self, config_file, key, value):
        lines = []
        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                for line in f:
                    if "=" in line:  # Ensure the line contains a key-value pair
                        k, v = line.strip().split("=", 1)
                        if k == key:
                            line = f"{key}={value}\n"
                    lines.append(line)
        else:
            lines.append(f"{key}={value}\n")

        with open(config_file, "w") as f:
            f.writelines(lines)

    def build_arguments(self):
        if self.__operation in ["create-entity", "create-test"]:
            if not self.__entity_name or not self.__project_repo:
                print("\033[31mERROR: Missing required arguments for the operation.\033[0m")
                exit(1)
            # Build the correct order for TCL script arguments
            tcl_args = [self.__entity_name, self.__project_repo]
        elif self.__operation == "check-syntax":
            if not self.__project_repo:
                print("\033[31mERROR: Missing required argument '--path' for check-syntax.\033[0m")
                exit(1)
            tcl_args = [self.__project_repo]
        elif self.__operation in ["export-xsa"]:
            tcl_args = [self.__project_repo]
        else:
            tcl_args = []

        return self.__operation, self.__vivado_path, tcl_args
