from modules.calculations.mult import mult


def div(number_1, number_2):
    if number_2 != [0, 0]:
        answer = [0, 0]
        number_1 = mult(number_1, [number_2[0], -(number_2[1])])
        number_2 = mult(number_2, [number_2[0], -(number_2[1])])
        answer[0] = number_1[0] / number_2[0]
        answer[1] = number_1[1] / number_2[0]
        return answer
    else:
        # print("На ноль делить нельзя!!!")
        return number_1

