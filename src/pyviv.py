import PyVivConfig
import PyVivExecutor

def main():
    config = PyVivConfig.PyVivConfig()
    executor = PyVivExecutor.PyVivExecutor()

    operation, vivado_path, tcl_args = config.build_arguments()
    if operation != "add-path" and operation != "add-vivado":
        executor.run_tcl_script(operation, vivado_path, tcl_args)

if __name__ == "__main__":
    main()
