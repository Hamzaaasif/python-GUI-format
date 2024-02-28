# Python GUI Templaate
## Prerequisites

- Python 3.x installed on your system
- Virtual environment (venv) module installed

## Setup

1. Clone the repository to your local machine.
2. Navigate to the project directory.

## Create and Activate Virtual Environment

1. Open a terminal or command prompt.
2. Create a virtual environment by running the following command:
    ```
    python -m venv myenv
    ```
3. Activate the virtual environment:
    - On Windows:
      ```
      myenv\Scripts\activate
      ```
    - On macOS and Linux:
      ```
      source myenv/bin/activate
      ```

## Install Required Packages

1. Make sure you are in the project directory and the virtual environment is activated.
2. Install the required packages by running the following command:
    ```
    pip install -r requirements.txt
    ```

# 1- Logging
using [Loguru](https://github.com/Delgan/loguru) python package for loggin 
### For Information
```
logger.info("This is info")
```
### For Debug
```
logger.debug(f"This is input file: {input_file}")
```
### For Error
```
logger.error("Error occured, check error.txt")
```

# 2- Installation

```
pip install -r requirements.txt
```

# 3- GUI
Using [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) for graphical user interface. Add layout according to your need. 
For printing in pyGuiSimple output, use `print`

```
print("This will print in PyGuiSimple output console")
```

# 4- Generating standalone executable files

## For Windows
```
pyinstaller.exe --onefile ./<PYTHON_FILE_NAME>.py
```

## For MacOS

### Updated Method
```
pyinstaller --onefile --icon=PATH_TO_ICON gui.py
```
### OLD METHOD
```
python3 -m PyInstaller --windowed ./<PYTHON_FILE_NAME>.py

--- The issue 

pyinstaller --windowed myapp.py
cd dist/myapp.app/Contents/MacOs
mkdir tcl tk
cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/tcl* tcl/
cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/tk* tk/
cp -R /Library/Frameworks/Python.framework/Versions/3.7/lib/Tk* tk/ 

```
The executable file will be found in script->script.app(show contained files)->MacOs->script.app
