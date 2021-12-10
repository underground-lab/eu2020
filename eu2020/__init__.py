import logging
import re
import os
from rich.console import Console
from rich.theme import Theme


WIDTH = 80
HEIGHT = 20
LOGFILE = 'eu2020.log'
WRITE_LOG = True


def print_log(text, print=True, log=True):
    if print:
        console.print(text)
    if WRITE_LOG and log:
        t = re.sub(r'\[[^\[]*\]', '', text)
        logging.info(t)


# pytest doesn't like os.get_terminal_size()
try:
    (WIDTH, HEIGHT) = os.get_terminal_size()
except Exception:
    print("get_terminal_size error")

logging.basicConfig(filename=LOGFILE, filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
console = Console(theme=Theme(inherit=False), width=WIDTH)
