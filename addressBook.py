from collections import UserDict
from datetime import datetime, timedelta
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Невірний формат номера телефону.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            date = datetime.strptime(value, "%d.%m.%Y")
            self.value = date
        except ValueError:
            raise ValueError("Невірний формат дати. Використовуйте ДД.ММ.РРРР")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[i] = Phone(new_phone)
                break

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return str(p)
        return None

    def add_birthday(self, birthday):
        if self.birthday is not None:
            raise ValueError("Можна додати тільки одне поле дня народження.")
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Ім'я контакту: {self.name.value}, телефони: {'; '.join(str(p) for p in self.phones)}, день народження: {str(self.birthday)}" if self.birthday else f"Ім'я контакту: {self.name.value}, телефони: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.now().date()
        next_week = today + timedelta(days=7)
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday and today <= record.birthday.value.date() < next_week:
                upcoming_birthdays.append(record)
        return upcoming_birthdays