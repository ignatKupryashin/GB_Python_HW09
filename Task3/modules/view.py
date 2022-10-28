import csv
from telebot import TeleBot


def view_note(msg):
    bot = TeleBot("5679603314:AAHWRut6ZCpLYgTEHMo-pDqQvtUahdwqjAM")
    counter = int(1)
    with open('database.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bot.send_message(chat_id=msg.from_user.id, text= str(counter) + ". " + str(row["Фамилия"]) + " "
                                                            + str(row["Имя"]) + " " + str(row["Телефон"]) + " "
                                                            + str(row["Описание"]))
            counter += 1