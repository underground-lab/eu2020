import logging
import re
from rich.console import Console
from rich.theme import Theme


WIDTH = 80
LOGFILE = 'eu2020.log'
WRITE_LOG = True

def printlg(text, print=True, log=True):
    if print is True:
        console.print(text)
    if WRITE_LOG is True and log is True:
        t = re.sub(r'\[[^\[]*\]', '', text)
        logging.info(t)


logging.basicConfig(filename=LOGFILE, filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
console = Console(theme=Theme(inherit=False), width=WIDTH)
