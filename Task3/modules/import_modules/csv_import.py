import csv
from modules.add_note import add_note


def csv_import(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        counter = 0
        for row in reader:
            add_note(row["Фамилия"], row["Имя"], row["Телефон"], row["Описание"])
            counter += 1
    print(f"Импортировано записей: {counter}")