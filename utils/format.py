from datetime import datetime
from colorama import Fore, Style

def info(message):
    info_format = f"{Fore.YELLOW}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET} {Style.NORMAL}[{Fore.CYAN}INFO{Fore.RESET}]{Style.RESET_ALL} "
    print(f"{info_format}{message}")

def error(message):
    error_format = f"{Fore.YELLOW}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET} {Style.NORMAL}[{Fore.RED}ERROR{Fore.RESET}]{Style.RESET_ALL} "
    print(f"{error_format}{message}")
