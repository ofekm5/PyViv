# vhdl-ip-wrapper

**VHDL IP Wrapper** is a Python tool designed to streamline the process of wrapping VHDL files into IP packages using Xilinx Vivado. The tool simplifies IP creation by providing a Python script interface that runs a customizable TCL script under the hood. This is useful for automating repetitive tasks, ensuring consistency, and making IP packaging workflows accessible across multiple projects.

---

## Features

- **Command-line Interface (CLI):** Use the tool directly from the terminal with arguments.
- **Vivado Integration:** Runs Vivado in batch mode to package VHDL files as IP cores.
- **Customizable Workflow:** Includes a base TCL script (`wrap_vhdl_as_ip.tcl`) that can be modified to fit specific project needs.
- **Cross-Project Usability:** Installable in editable mode to allow easy use across multiple Python projects.

---

## Installation

### Prerequisites
- Python 3.6 or later
- Xilinx Vivado installed on your system
- Pip (`pip install setuptools` if not already installed)

### Steps to Install Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/vhdl-ip-wrapper.git
   cd vhdl-ip-wrapper
   ```

2. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

---

## Usage

### Command-line Interface
Once installed, the tool can be run using the `vhdl-ip-wrapper` command:
```bash
vhdl-ip-wrapper <vhdl_file> <ip_dir> --vivado <vivado_path>
```

#### Arguments:
- `<vhdl_file>`: Path to the VHDL file you want to package.
- `<ip_dir>`: Output directory for the IP package.
- `--vivado`: (Optional) Path to the Vivado executable. Default: `vivado`.

#### Example:
```bash
vhdl-ip-wrapper "C:/path/to/entity.vhd" "C:/path/to/ip_package" --vivado "C:/Xilinx/Vivado/2024.1/bin/vivado.bat"
```

### As a Python Library
You can also use the tool as a library in Python scripts:
```python
from vhdl_ip_wrapper.main import run_vivado

run_vivado(
    vhdl_file="C:/path/to/entity.vhd",
    ip_dir="C:/path/to/ip_package",
    vivado_path="C:/Xilinx/Vivado/2024.1/bin/vivado.bat"
)
```

---

## File Structure

```
vhdl_ip_wrapper/
├── vhdl_ip_wrapper/
│   ├── __init__.py              # Makes the package importable
│   ├── main.py                  # Core Python script
│   ├── wrap_vhdl_as_ip.tcl      # Customizable TCL script for Vivado
├── setup.py                     # Package metadata and installation configuration
├── README.md                    # Project documentation
├── LICENSE                      # License file
├── requirements.txt             # Project dependencies (if any)
```

---

## Development

### Running Locally
To test the tool locally without installing:
```bash
python vhdl_ip_wrapper/main.py <vhdl_file> <ip_dir> --vivado <vivado_path>
```

### Modifying the TCL Script
Edit `wrap_vhdl_as_ip.tcl` to customize the Vivado workflow. This script is the core of the IP packaging process.

---

## Troubleshooting

1. **Vivado Not Found:**
   Ensure Vivado is installed and its path is correctly passed using the `--vivado` flag.
   
2. **Permission Issues:**
   Make sure you have write permissions for the IP output directory.

3. **Syntax Errors in TCL Script:**
   Modify `wrap_vhdl_as_ip.tcl` to resolve specific Vivado compatibility issues.

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Before submitting, ensure your code adheres to the project's style and passes basic tests.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- [Xilinx Vivado](https://www.xilinx.com/products/design-tools/vivado.html) for providing the tools that made this project possible.
- The open-source community for inspiration and best practices.