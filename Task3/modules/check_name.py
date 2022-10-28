def check_name(name):
    abbadonned_symbols = [",", "\\", "/", ":", "*", "?", "\"", "<", ">", "|", "+", "%", "!", " "]
    for i in abbadonned_symbols:
        if i in name:
            print("Введённое имя содержит недопустимые символы")
            return False
    return name
