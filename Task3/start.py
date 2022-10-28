from modules.view import view_note
from modules.add_note import add_note
from modules.add_note_checker import check_tel
import csv
from telebot import TeleBot
from telebot import types
from modules.export_modules.xml_generator import create_xml
from modules.export_modules.txt_generator import create_txt
from modules.export_modules.csv_generator import create_csv


bot = TeleBot("5679603314:AAHWRut6ZCpLYgTEHMo-pDqQvtUahdwqjAM")
dict = {"Фамилия": None, "Имя": None, "Телефон": None, "Описание": None}


@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(chat_id=msg.from_user.id, text="Телефонный справочник запущен")
    try:
        file = open("database.csv", "r")
        file.close()
    except:
        with open("database.csv", 'w', newline='') as csvfile:
            fieldnames = ["Фамилия", "Имя", "Телефон", "Описание"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    view_note_interface_button = types.KeyboardButton("Просмотреть справочник")
    add_note_button = types.KeyboardButton("Добавить запись")
    export_interface_button = types.KeyboardButton("Экспорт справочника")
    import_interface_button = types.KeyboardButton("Импорт справочника")
    main_rmk = types.ReplyKeyboardMarkup()
    main_rmk.add(view_note_interface_button,add_note_button,export_interface_button,import_interface_button)
    bot.send_message(chat_id=msg.from_user.id, text=f"Выберете операцию", reply_markup=main_rmk)




def input_surname(msg):
    global dict
    dict["Фамилия"] = msg.text.capitalize()
    next_message = bot.send_message(chat_id=msg.from_user.id, text="Введите имя")
    bot.register_next_step_handler(callback=input_name, message=next_message)

def input_name(msg):
    global dict
    dict["Имя"] = msg.text.capitalize()
    next_message = bot.send_message(chat_id=msg.from_user.id, text="Введите телефон")
    bot.register_next_step_handler(callback=input_tel, message=next_message)

def input_tel(msg):
    global dict
    tel = check_tel(msg.text)
    if tel:
        dict["Телефон"] = tel
        next_message = bot.send_message(chat_id=msg.from_user.id, text="Введите описание")
        bot.register_next_step_handler(callback=input_discription, message=next_message)
    else:
        next_message = bot.send_message(chat_id=msg.from_user.id, text="Введён некорректный телефон\nВведите телефон")
        bot.register_next_step_handler(callback=input_tel, message=next_message)

def input_discription(msg):
    global dict
    dict["Описание"] = msg.text
    add_note(dict["Фамилия"], dict["Имя"], dict["Телефон"], dict["Описание"])
    bot.send_message(chat_id=msg.from_user.id, text=f"Данные внесены")


def export_interface(msg):
    csv_button = types.KeyboardButton("csv")
    xml_button = types.KeyboardButton("xml")
    txt_button = types.KeyboardButton("txt")
    export_rmk = types.ReplyKeyboardMarkup()
    export_rmk.add(csv_button,xml_button,txt_button)
    next_message = bot.send_message(chat_id=msg.from_user.id, text=f"Выберете формат", reply_markup=export_rmk)
    bot.register_next_step_handler(message=next_message, callback=choose_export)

def choose_export(msg):
    bot.send_message(chat_id=msg.from_user.id, text=f"Начало экспорта")
    if msg.text == "csv":
        bot.send_message(chat_id=msg.from_user.id, text=f"Экспортирую csv")
        create_csv()
        bot.send_document(chat_id=msg.from_user.id, document=open("export/data.csv", "rb"))
    elif msg.text == "xml":
        create_xml()
        bot.send_document(chat_id=msg.from_user.id, document=open("export/data.xml", "rb"))
    elif msg.text == "txt":
        create_txt()
        bot.send_document(chat_id=msg.from_user.id, document=open("export/data.txt", "rb"))
    start


def


@bot.message_handler()
def main_interface(msg):
    if msg.text == "Просмотреть справочник":
        view_note(msg)
    elif msg.text == "Добавить запись":
        next_message = bot.send_message(chat_id=msg.from_user.id, text=f"Введите фамилию:")
        bot.register_next_step_handler(callback=input_surname, message=next_message)
    elif msg.text == "Экспорт справочника":
        export_interface(msg)
    elif msg.text == "Импорт справочника":
        pass


bot.infinity_polling()