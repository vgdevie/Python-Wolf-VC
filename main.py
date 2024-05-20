from colorama import Fore, Style, Back # type: ignore
import subprocess
import os

# Define the options
options = [
    {"name": "Тема 4 Завдання 1", "fileName": "topic4task1.py"},
    {"name": "Тема 4 Завдання 2", "fileName": "topic4task2.py"},
    {"name": "Тема 4 Завдання 3", "fileName": "topic4task3.py"},
    {"name": "Тема 4 Завдання 4", "fileName": "topic4task4.py"},
    {"name": "Тема 6 Завдання 1", "fileName": "topic6task1.py"},
    {"name": "Тема 6 Завдання 2", "fileName": "topic6task2.py"},
    {"name": "Тема 6 Завдання 3", "fileName": "topic6task3.py"},
    {"name": "Тема 6 Завдання 4", "fileName": "topic6task4.py"},
    {"name": "Тема 8 Завдання 1", "fileName": "topic8task1.py"},
    {"name": "Тема 8 Завдання 2", "fileName": "topic8task2.py"},
    {"name": "Тема 8 Завдання 4", "fileName": "topic8task4.py"},
    {"name": "Тема 9 Завдання 1", "fileName": "topic9task1.py"},
    {"name": "Тема 10 Завдання 1", "fileName": "topic10task1.py"},
    {"name": "Тема 10 Завдання 2", "fileName": "topic10task2.py"},
    {"name": "Тема 12 Завдання 1", "fileName": "topic12task1.py"},
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
    print("WOOLF University")
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