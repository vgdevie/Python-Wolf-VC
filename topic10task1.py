from addressBook import AddressBook, Record

# Перевірка роботи коду
book = AddressBook()

john_record = Record("Джон")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("01.01.1990")
book.add_record(john_record)

jane_record = Record("Джейн")
jane_record.add_phone("9876543210")
jane_record.add_birthday("15.05.1985")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("Джон")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}")

book.delete("Джейн")

upcoming_birthdays = book.get_upcoming_birthdays()
for record in upcoming_birthdays:
    print(f"День народження: {record.birthday.value.date()}, Ім'я контакту: {record.name.value}")
