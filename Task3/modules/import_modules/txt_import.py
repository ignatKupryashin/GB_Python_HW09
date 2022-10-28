from modules.add_note import add_note


def txt_import(filename):
    def new_string(file):
        string = file.readline
    counter = 0
    with open(filename, "r") as file:
        flag = True
        while flag:
            current_string = file.readline()
            if current_string == "":
                flag = False
            current_string = current_string.replace("\n", "")
            if current_string == "":
                continue
            else:
                family = current_string
                name = file.readline().replace("\n", "")
                tel = file.readline().replace("\n", "")
                discription = file.readline().replace("\n", "")
                if "Фамилия: " in family and "Имя: " in name and "Телефон: " in tel and "Описание: " in discription:
                    family = family.replace("Фамилия: ", "")
                    name = name.replace("Имя: ", "")
                    tel = tel.replace("Телефон: ", "")
                    discription = discription.replace("Описание: ", "")
                    add_note(family, name, tel, discription)
                    counter += 1
                else:
                    print("Файл повреэждён. Импорт невозможен")
                    continue
    print(f"Импортировано записей: {counter}")