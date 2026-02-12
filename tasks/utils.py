from colorama import Fore, Style


def print_error(message: str) -> None:
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")
