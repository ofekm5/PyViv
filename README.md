# PyViv

**PyViv** is a Python tool designed to enhance VHDL development by providing a simple and efficient interface for common tasks such as adding VHDL entities, running syntax checks, and integrating Vivado TCL scripts. It simplifies workflows for developers working with Xilinx Vivado, offering pre-defined operations and customizable scripts to suit project needs.

---

## Features

- **Command-line Interface (CLI):** Easily perform tasks such as adding VHDL files, syntax checks, and testbench creation directly from the command line.
- **Seamless Vivado Integration:** Automates Vivado operations in batch mode using TCL scripts for streamlined workflows.
- **Customizable TCL Scripts:** Add or modify TCL scripts in the `scripts` folder to tailor Vivado project management to your needs.
- **Predefined VHDL Templates:** Automatically generate VHDL files with standardized templates to maintain code consistency and quality.

---

## Installation

### 1. Installing PyViv

You can install **PyViv** in two ways:

#### Option 1: Standard Installation (Recommended for Users)
This method installs PyViv as a regular package without linking it to the source code.

```bash
pip install .
```

Once installed, you can use PyViv from anywhere in your terminal.

#### Option 2: Editable Installation (Recommended for Developers)
If you plan to modify PyViv's source code and want changes to reflect immediately, install it in **editable mode**:

```bash
pip install -e .
```

In this mode, PyViv is linked to your local source directory, and changes made to the code are reflected instantly without the need for reinstallation.

---

### 2. Switching Between Installation Modes

If you installed PyViv in one mode and want to switch to the other:

#### Switching from Editable to Standard Mode
1. Uninstall the current editable version:
   ```bash
   pip uninstall pyviv
   ```
2. Reinstall PyViv as a standard package:
   ```bash
   pip install .
   ```

#### Switching from Standard to Editable Mode
1. Uninstall the standard installation:
   ```bash
   pip uninstall pyviv
   ```
2. Reinstall in editable mode for development:
   ```bash
   pip install -e .
   ```

---

After installation, you can verify by running:

```bash
pyviv --help
```

This will display usage information and confirm that PyViv is installed correctly.

## Usage

Once installed, PyViv can be accessed globally via the `pyviv` command:

```bash
pyviv <operation> [options]
```

### Available Commands

- **Set project path:**  
  Set the project repository path for future commands.  
  ```bash
  pyviv add-path --path "C:/path/to/your/project"
  ```

- **Create a new VHDL entity:**  
  Automatically creates an entity file with a pre-defined template.  
  ```bash
  pyviv create-entity --entity EntityName
  ```

- **Create a new testbench:**  
  Generates a testbench for the specified entity.  
  ```bash
  pyviv create-test --entity EntityName
  ```

- **Check VHDL syntax:**  
  Runs Vivado syntax checking on project sources.  
  ```bash
  pyviv check-syntax
  ```

---

## Contribution

We welcome contributions to PyViv! If you'd like to improve the tool, please follow these guidelines:

1. **Adding New Features:**  
   - Open an issue describing the feature you'd like to add.
   - Discuss potential improvements before implementation.

2. **Contributing TCL Scripts:**  
   - Add new TCL scripts to the `scripts` folder.
   - Ensure your script is well-documented and follows the existing format.

3. **Bug Reports & Feature Requests:**  
   - Report bugs and suggest new features via GitHub issues.

---

## Project Structure

```
PyViv/
├── src/
│   ├── __init__.py              # Makes the package importable
│   ├── pyviv.py                 # Main CLI entry point
│   ├── PyVivConfig.py           # Handles CLI arguments and project path
│   ├── PyVivExecutor.py         # Handles execution of Vivado TCL scripts
│   ├── scripts/                 # Folder containing all TCL scripts
├── setup.py                     # Installation configuration
├── README.md                    # Documentation
├── LICENSE                      # Project license
```

---

## Troubleshooting

1. **Vivado Not Found:**  
   Ensure that Vivado is correctly installed and its path is properly set.

2. **Permission Issues:**  
   Ensure you have the necessary permissions to add files to the project directory.

3. **Syntax Errors in TCL Scripts:**  
   Check for syntax errors or typos in the TCL scripts inside the `scripts/` folder.

---

## License

This project is licensed under the [MIT License](LICENSE).


---

## Acknowledgments

I would like to express my deep appreciation to Dr. Shir Landau-Feibish and the Open University of Israel for providing me with the platform and opportunity to create and develop **PyViv**. Their support and resources have been instrumental in bringing this project to life.

Special thanks to:

- [Xilinx Vivado](https://www.xilinx.com/products/design-tools/vivado.html) for offering robust tools that make FPGA development accessible.
- The open-source community for continuous inspiration, collaboration, and sharing of best practices.

---
