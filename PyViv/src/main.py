import PyVivConfig 
import PyVivExecutor

# Example Usage:
# python main.py add-path --path "/path/to/project/repo"
# python main.py create-test --entity TempValidatortwoTB --path "C:\Users\avita\source\repos\ofekm5\ZeroRttTcp\ClientNIC\TcpDetector"
# python main.py check-syntax --path "C:\Users\avita\source\repos\ofekm5\ZeroRttTcp\ClientNIC\TcpDetector"
# python main.py create-entity --entity ReservedValidator --path "C:\Users\avita\source\repos\ofekm5\ZeroRttTcp\ClientNIC\TcpDetector"

def main():
    config = PyVivConfig.PyVivConfig()
    executor = PyVivExecutor.PyVivExecutor()

    operation, vivado_path, tcl_args = config.build_arguments()
    executor.run_tcl_script(operation, vivado_path, tcl_args)

if __name__ == "__main__":
    main()
