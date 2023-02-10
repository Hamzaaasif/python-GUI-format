# Python GUI Templaate

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