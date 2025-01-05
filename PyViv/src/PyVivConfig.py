import argparse
import os

class PyVivConfig:
    def __init__(self):
        self.__pyviv_operations = ["create-entity", "create-test", "check-syntax", "add-path"]
        parser = argparse.ArgumentParser(description="PyViv: A VHDL Management Tool")
        parser.add_argument("operation", choices=self.__pyviv_operations, help="Operation to perform (e.g., create-entity, create-test, check-syntax, add-path).")
        parser.add_argument("--vivado", default="C:/Xilinx/Vivado/2024.1/bin/vivado.bat", help="Path to the Vivado executable (default: 'vivado').")
        parser.add_argument("--entity", help="Name of the VHDL entity (required for create-entity and create-test).")
        parser.add_argument("--path", help="Override the project repository path.")
        args = parser.parse_args()

        self.__vivado_path = args.vivado
        self.__operation = args.operation

        if args.operation == "add-path":
            if not args.path:
                print("\033[31mERROR: '--path' is required for 'add-path'.\033[0m")
                exit(1)
            self.__set_project_repo_path(args.path)
            return

        self.__project_repo = self.__get_project_repo_path(args.path)

        if args.operation in ["create-entity", "create-test"] and not args.entity:
            print(f"\033[31mERROR: '--entity' is required for '{args.operation}'.\033[0m")
            exit(1)

        self.__operation = args.operation
        self.__entity_name = args.entity

    def __get_project_repo_path(self, path_override=None):
        config_file = os.path.expanduser("~/.pyviv_config")
        if path_override:
            return path_override

        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                return f.read().strip()

        print("\033[31mERROR: Project repository path is not set. Use 'add-path' to set it or pass '--path'.\033[0m")
        exit(1)

    def __set_project_repo_path(self, path):
        config_file = os.path.expanduser("~/.pyviv_config")
        with open(config_file, "w") as f:
            f.write(path)
        print(f"\033[32mINFO: Project repository path set to '{path}'.\033[0m")

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
        else:
            tcl_args = []

        return self.__operation, self.__vivado_path, tcl_args
