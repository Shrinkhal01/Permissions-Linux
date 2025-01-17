# File Permission Calculator (CLI)

## Description
This Python-based **File Permission Calculator** allows users to easily convert file permissions (in the standard `rwxrwxrwx` format) into their corresponding numeric values (e.g., `755`, `644`). It provides a simple and efficient way to calculate file permission values as typically seen in Unix-based systems like Linux and macOS.

The program currently works via the **command-line interface (CLI)**. In the future, the tool will be expanded to include a **graphical user interface (GUI)** for even easier interaction.

## Features
- **CLI-based input**: Users input file permissions in the standard `rwxrwxrwx` format (e.g., `rwxr-xr--`).
- **Numeric permission calculation**: The program calculates the numeric equivalent (e.g., `755`, `644`) based on the input permission string.
- **Simple and intuitive**: Easily calculates permissions in one step.

## Example Usage

1. Clone or download the repository.
2. Run the script from the command line.

Example of input/output:

```bash
$ python permission_calculator.py
File Permission Calculator (like `rwxr-xr--` format)
Enter permissions in `rwxrwxrwx` format (e.g., rwxr-xr--): rwxr-xr--
Numeric Permission: 755
```

## Installation
To use the File Permission Calculator, you’ll need Python installed on your system. This script works with Python 3.x.

### Steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/file-permission-calculator.git
    cd file-permission-calculator
    ```
2. Install dependencies: There are no external dependencies at this time. The script uses only the Python standard library.

3. Run the script:
    ```bash
    python permission_calculator.py
    ```
    Enter the file permissions when prompted in the `rwxrwxrwx` format.

    
