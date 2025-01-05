import PyVivConfig 
import PyVivExecutor

# Example Usage:
# python src/main.py add-path --path "C:\Users\avita\source\repos\ofekm5\ZeroRttTcp\ClientNIC\TcpDetector"
# python src/main.py create-test --entity TempValidatortwoTB --path "C:\Users\avita\source\repos\ofekm5\ZeroRttTcp\ClientNIC\TcpDetector"
# python src/main.py check-syntax --path "C:\Users\avita\source\repos\ofekm5\ZeroRttTcp\ClientNIC\TcpDetector"
# python src/main.py create-entity --entity ReservedValidator --path "C:\Users\avita\source\repos\ofekm5\ZeroRttTcp\ClientNIC\TcpDetector"

def main():
    config = PyVivConfig.PyVivConfig()
    executor = PyVivExecutor.PyVivExecutor()

    operation, vivado_path, tcl_args = config.build_arguments()
    if operation != "add-path":
        executor.run_tcl_script(operation, vivado_path, tcl_args)

if __name__ == "__main__":
    main()
