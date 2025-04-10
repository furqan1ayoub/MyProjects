# Leaks Formatter

This project is a simple Python script designed to process and format login data from a file. It reads an input file containing raw login information, extracts valid entries, and saves them in a clean, readable format.

## Features

- Parses login data from a file.
- Formats valid entries as `username -> password`.
- Skips malformed lines and logs them to the console.
- Handles file-related errors gracefully.

## Requirements

- Python 3.x installed on your system.
- An input file named `100mLogins.txt` in the same directory as the script.

## How to Use

1. Place your input file (`100mLogins.txt`) in the same directory as the script.
2. Run the script using the following command:
   ```bash
   python script1.py

3. When prompted, enter the desired name for the output file (without the extension).
4. The script will create a new .txt file with the formatted data.


# Notes
The script ignores encoding errors in the input file.
Make sure the input file is in the same directory as the script.
The output file will be appended if it already exists.
# License
**This project is open-source and free to use. Feel free to modify it as needed.**