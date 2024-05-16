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
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Контакт оновлено."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}
    print("Ласкаво просимо до бота-помічника!")
    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)

        if command in ["закрити", "вийти"]:
            print("До побачення!")
            break
        elif command == "привіт":
            print("Як я можу допомогти?")
        elif command == "додати":
            print(add_contact(args, contacts))
        elif command == "змінити":
            print(change_contact(args, contacts))
        elif command == "телефон":
            print(show_phone(args, contacts))
        elif command == "всі":
            show_all(contacts)
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()
