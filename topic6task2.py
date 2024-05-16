def generate_cats_file(path):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write("1,Whiskers,3\n")
            file.write("2,Fluffy,5\n")
            file.write("3,Max,2\n")
    except Exception as e:
        print(f"Помилка: {str(e)}")

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {str(e)}")
    return cats_info

generate_cats_file("data/cats_file.txt")
cats_info = get_cats_info("data/cats_file.txt")
print(cats_info)


