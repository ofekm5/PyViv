import PyVivConfig 
import PyVivExecutor

# Example Usage:
# pyviv add-path --path "/path/to/project/repo"
# pyviv create-entity --entity MyEntity
# pyviv create-test --entity MyEntity
# pyviv check-syntax
# pyviv create-entity --entity MyEntity --path "/different/path"

def main():
    config = PyVivConfig.PyVivConfig()
    executor = PyVivExecutor.PyVivExecutor()

    tcl_args = config.build_arguments()
    executor.run_tcl_script(tcl_args)

if __name__ == "__main__":
    main()
