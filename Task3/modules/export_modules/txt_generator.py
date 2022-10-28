import csv


def create_txt(name="data"):
    with open('database.csv', newline='') as csvfile:
        txt = ""
        reader = csv.DictReader(csvfile)
        page = open(f"export/{name}.txt", 'w')
        for row in reader:
            txt += f'Фамилия: {row["Фамилия"]}\n'
            txt += f'Имя: {row["Имя"]}\n'
            txt += f'Телефон: {row["Телефон"]}\n'
            txt += f'Описание: {row["Описание"]}\n\n'
        page.write(txt)