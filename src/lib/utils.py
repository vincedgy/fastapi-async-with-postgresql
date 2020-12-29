import colorama
import logging

SEP: str = f"{colorama.Fore.LIGHTGREEN_EX}:{colorama.Fore.RESET}"
FORMAT: str = f"{colorama.Fore.LIGHTBLACK_EX}%(asctime)-15s{colorama.Fore.RESET}"
FORMAT += f"{SEP}"
FORMAT += f"{colorama.Fore.MAGENTA}%(levelname)s{colorama.Fore.RESET}"
FORMAT += f"{SEP}"
FORMAT += f"{colorama.Fore.LIGHTBLUE_EX}%(name)s{colorama.Fore.RESET}"
FORMAT += f"{SEP}"
FORMAT += f"{colorama.Fore.WHITE}%(message)s{colorama.Fore.RESET}"

logging.basicConfig(format=FORMAT, level=logging.INFO)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name=name)


# Test function for module
def _test():
    assert get_logger is logging


if __name__ == '__main__':
    _test()
