import random
import sys
import time
from datetime import datetime

from colorama import Fore, Style


def slowprint(message):
    for letter in message + "\n":
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.randint(8, 9) / 1000)


def info(message):
    info_format = f"{Fore.YELLOW}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET} {Style.NORMAL}[{Fore.CYAN}INFO{Fore.RESET}]{Style.RESET_ALL} "
    slowprint(f"{info_format}{message}")


def error(message):
    error_format = f"{Fore.YELLOW}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET} {Style.NORMAL}[{Fore.RED}ERROR{Fore.RESET}]{Style.RESET_ALL} "
    slowprint(f"{error_format}{message}")
