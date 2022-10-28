import csv


def add_note(family=None, name=None, tel=None, discription=None):
    with open("database.csv", "a", newline="") as csvfile:
        fieldnames = ["Фамилия", "Имя", "Телефон", "Описание"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Фамилия": family, "Имя": name, "Телефон": tel, "Описание": discription})

