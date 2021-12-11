import logging
import re
import shutil

from rich.console import Console
from rich.theme import Theme

WIDTH, HEIGHT = shutil.get_terminal_size(fallback=(80, 20))
LOGFILE = 'eu2020.log'
WRITE_LOG = True


def print_log(text, print=True, log=True):
    if print:
        console.print(text)
    if WRITE_LOG and log:
        t = re.sub(r'\[[^\[]*\]', '', text)
        logging.info(t)


logging.basicConfig(filename=LOGFILE, filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
console = Console(theme=Theme(inherit=False), width=WIDTH)

print_log(f"terminal size: {WIDTH} x {HEIGHT}", print=False)
