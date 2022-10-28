def print_number(number):
    answer = ""
    if number[0] != 0:
        answer += str(number[0])
    if number[1] != 0:
        if number[1] > 0:
            answer += f"+{number[1]}i"
        else:
            answer += f"{number[1]}i"
    if answer == "":
        return "0"
    else:
        return answer
