from colorama import Fore, Style, Back # type: ignore
import subprocess
import os

# Define the options
options = [
    {"name": "Тема 4 Завдання 1", "fileName": "topic4task1.py"},
    {"name": "Тема 4 Завдання 2", "fileName": "topic4task2.py"},
    {"name": "Тема 4 Завдання 3", "fileName": "topic4task3.py"},
    {"name": "Тема 4 Завдання 4", "fileName": "topic4task4.py"}
]

def print_menu():
    os.system('clear') 
    print(Style.RESET_ALL)
    print(Fore.WHITE + "▓██     ░██░     ██▒")
    print(Fore.WHITE + " ███    ████    ███ ")
    print(Fore.WHITE + " ░██░  ▒████▒  ▒██░ ")
    print(Fore.WHITE + "  ███ ░██  ██  ██▓  ")
    print(Fore.WHITE + "   ██▓        ▓██   ")
    print(Fore.WHITE + "   ░██       ░██░")
    print(Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT)
    print("====================")
    print("Viacheslav Chukhno")
    print("Python Course")
    print("WOLF University")
    print("2024")
    print("====================")
    print(Style.RESET_ALL)
    for i, option in enumerate(options, 1):
        print(Fore.GREEN + f"{i}. {option['name']}" + Style.RESET_ALL)
    print(Fore.RED + f"{len(options) + 1}. Exit" + Style.RESET_ALL)

def run_option(option):
    subprocess.call(["python", option['fileName']])

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            run_option(options[int(choice) - 1])
        elif choice == str(len(options) + 1):
            break
        else:
            print(Fore.RED + "Invalid choice. Please choose a valid option." + Style.RESET_ALL)

if __name__ == "__main__":
    main()