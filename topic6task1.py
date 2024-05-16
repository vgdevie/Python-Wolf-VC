import random

def generate_test_file(path, num_records):
    with open(path, 'w', encoding='utf-8') as file:
        for _ in range(num_records):
            name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
            salary = random.randint(10000, 30000)
            file.write(f"{name},{salary}\n")

def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1

        average = total / count

        return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None

    except Exception as e:
        print(f"Помилка: {str(e)}")
        return None


generate_test_file("data/salary_file.txt", 10)
total, average = total_salary("data/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
