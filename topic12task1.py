from addressBook import AddressBook, Record
from datetime import datetime, timedelta
import pickle

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не знайдено."
        except ValueError:
            return "Невірна кількість аргументів. Потрібно вказати ім'я та номер телефону."
        except IndexError:
            return "Невірна кількість аргументів. Потрібно вказати ім'я."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, address_book):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return "Контакт додано."

@input_error
def change_contact(args, address_book):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    record = address_book.find(name)
    if record:
        record.edit_phone(record.phones[0].value, phone)
        return "Контакт оновлено."
    else:
        raise KeyError

@input_error
def show_phone(args, address_book):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    record = address_book.find(name)
    if record:
        return '; '.join(str(phone) for phone in record.phones)
    else:
        raise KeyError

@input_error
def add_birthday(args, address_book):
    if len(args) != 2:
        raise ValueError
    name, birthday = args
    record = address_book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Дата народження додана."
    else:
        raise KeyError

@input_error
def show_birthday(args, address_book):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    record = address_book.find(name)
    if record:
        return record.birthday
    else:
        raise KeyError

def show_all(address_book):
    for name, record in address_book.data.items():
        print(f"{name}: {'; '.join(str(phone) for phone in record.phones)}")

def birthdays(address_book):
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    for name, record in address_book.data.items():
        if record.birthday and today <= record.birthday <= next_week:
            print(f"{name}: {record.birthday}")

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    # Завантажуємо дані з файлу
    address_book = load_data()
    print("Ласкаво просимо до бота-помічника!")
    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)

        if command in ["закрити", "вийти"]:
            # Зберігаємо дані перед виходом з програми
            save_data(address_book)
            print("До побачення!")
            break
        elif command == "привіт":
            print("Як я можу допомогти?")
        elif command == "додати":
            print(add_contact(args, address_book))
        elif command == "змінити":
            print(change_contact(args, address_book))
        elif command == "телефон":
            print(show_phone(args, address_book))
        elif command == "додати-день-народження":
            print(add_birthday(args, address_book))
        elif command == "показати-день-народження":
            print(show_birthday(args, address_book))
        elif command == "всі":
            show_all(address_book)
        elif command == "дні-народження":
            birthdays(address_book)
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()