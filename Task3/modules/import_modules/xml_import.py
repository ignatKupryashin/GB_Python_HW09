from modules.add_note import add_note


def xml_import(filename):
    def new_string(file):
        string = file.readline
    counter = 0
    with open(filename, "r") as file:
        flag = True
        while flag:
            current_string = file.readline().replace("\n", "")
            if current_string == "</xml>":
                flag = False
                continue
            if current_string == "<xml>":
                continue
            if current_string == "":
                continue
            else:
                family = current_string
                name = file.readline().replace("\n", "")
                tel = file.readline().replace("\n", "")
                discription = file.readline().replace("\n", "")
                if "<Фамилия>" in family and "<Имя>" in name and "<Телефон>" in tel and "<Описание>" in discription:
                    family = family[family.index(">") + 1:family.rindex("<")]
                    name = name[name.index(">") + 1:name.rindex("<")]
                    tel = tel[tel.index(">") + 1:tel.rindex("<")]
                    discription = discription[discription.index(">") + 1:discription.rindex("<")]
                    add_note(family, name, tel, discription)
                    counter += 1
                else:
                    print("Файл повреждён. Импорт невозможен")
                    flag = False
    print(f"Импортировано записей: {counter}")