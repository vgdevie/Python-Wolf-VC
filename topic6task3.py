import sys
from pathlib import Path
from colorama import Fore, Style

def visualize_directory_structure(directory_path, indentation=""):
    directory = Path(directory_path)
    if not directory.exists() or not directory.is_dir():
        print(f"{Fore.RED}Невалідний шлях до директорії.{Style.RESET_ALL}")
        return

    for item in directory.iterdir():
        if item.is_dir():
            print(f"{Fore.BLUE}{indentation}📂 {item.name}{Style.RESET_ALL}")
            visualize_directory_structure(item, indentation + "  ")
        else:
            print(f"{Fore.GREEN}{indentation}📜 {item.name}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python topic6task3.py <шлях_до_директорії>{Style.RESET_ALL}")
    else:
        directory_path = sys.argv[1]
        visualize_directory_structure(directory_path)