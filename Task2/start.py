import datetime
from modules.checkers.check_command import check_command
from modules.checkers.check_number import check_number
from modules.calculate import calculate
from modules.print_number import print_number
from telebot import TeleBot

bot = TeleBot("5679603314:AAHWRut6ZCpLYgTEHMo-pDqQvtUahdwqjAM")

number = [0, 0]
current_operation = "+"

def my_log(message):
    my_string = f"{datetime.datetime.now()}--{print_number(number)}--{message.from_user.id}--{message.text}\n"
    with open("logger.txt", "a") as file:
        file.write(my_string)


@bot.message_handler(commands=["log"])
def my_log_export(msg):
    bot.send_document(chat_id=msg.from_user.id, document=open("logger.txt", "rb"))


@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(chat_id=msg.from_user.id, text=f"Добро пожаловать в лучший в мире калькулятор")
    bot.send_message(chat_id=msg.from_user.id, text=f"Текущее число {print_number(number)}")
    bot.send_message(chat_id=msg.from_user.id, text=f"Введите команду или новое число")

@bot.message_handler(commands=["help"])
def help(msg):
    bot.send_message(chat_id=msg.from_user.id, text=f"Программа Калькулятор.\n"
                                                    f" Может производить операции как с простыми, так и с комплексными числами.\n"
                                                    f"Комплексное число нужно записывать в формате n+ki (например 6-2i)\n"
                                                    f"Операциями являются:\n"
                                                    f" + -> сложить\n - -> отнять"
                                                    f"\n * -> умножить\n / -> разделить\n\n"
                                                    f"Для старта программы введите /start")


@bot.message_handler()
def interface(msg):
    global number
    my_log(msg)
    if check_number(msg.text) != "Ошибка":
        number = check_number(msg.text)
        next_message = bot.send_message(chat_id=msg.from_user.id, text="Число обновлено")
        bot.send_message(chat_id=msg.from_user.id, text=f"Текущее число {print_number(number)}")
        bot.send_message(chat_id=msg.from_user.id, text=f"Введите команду или новое число")
        bot.register_next_step_handler(callback=interface, message=next_message)
    elif check_command(msg.text):
        global current_operation
        current_operation = msg.text
        next_message = bot.send_message(chat_id=msg.from_user.id, text="Введите следующее число")
        bot.register_next_step_handler(next_message, calculations)


def calculations(msg):
    global number
    global current_operation
    if check_number(msg.text) != "Ошибка":
        number = calculate(number, check_number(msg.text), current_operation)
        next_message = bot.send_message(chat_id=msg.from_user.id, text="Расчёт произведён")
        bot.send_message(chat_id=msg.from_user.id, text=f"Текущее число {print_number(number)}")
        bot.send_message(chat_id=msg.from_user.id, text=f"Введите команду или новое число")
        bot.register_next_step_handler(next_message, interface)


bot.infinity_polling()