def check_complex_number(number):
    if number[-1] == "i":
        number = number[0:(len(number) - 1)]
        if number.isdigit:
            return int(number)
    return "Ошибка"
