import PySimpleGUI as sg
from loguru import logger
import traceback
import time


def gui():
    sg.theme('LightGreen3')
    layoutprefile = [
        [sg.Text('Select file to proceed') ],
        [sg.Text('Input '), sg.InputText(size=(91,2),change_submits=True), sg.FilesBrowse(size=12,button_color=('white', 'green'))],
        [sg.Output(size=(111, 15))],
        [sg.Submit('START',size=14,button_color=('white', 'green')) ,sg.Cancel('EXIT',size=14,button_color=('white', 'firebrick3'))]
    ]
    window = sg.Window('Scrape Data', layoutprefile,resizable=True)
    while True:
        event, values = window.read()
        if event in (None, 'EXIT', 'Cancel'):
            logger.info("Script exit success..")
            window.close()
            break
        elif event == 'START':
            file_path = values[0]
            if(file_path):
                start(file_path)
            else:
                logger.error("Please select input file")
            
            
def start(file_input):
    logger.info("Script started ... ")
    print("Script started ... ")
    try:    
        start_time = time.time()
        logger.debug(f"Reading input file: {file_input}")
        
        # your own functions and logic
        
        print("This prints on output of pyGuiSimple")
        
        end_time = time.time()
        total_time_spend = "{:.2f}".format((end_time-start_time))
        print(f"\nScript completed in {total_time_spend} seconds" )
        
    except:
        with open("error.txt", 'w') as errorFile:
            logger.error("Error occured, please check error.txt for more information..")
            traceback.print_exc(file=errorFile)
            
gui()
        