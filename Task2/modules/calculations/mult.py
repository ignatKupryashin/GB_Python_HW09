def mult(number_1, number_2):
    answer = [0, 0]
    answer[0] += number_1[0] * number_2[0]
    answer[0] += number_1[1] * number_1[1]
    answer[1] += number_1[0] * number_2[1]
    answer[1] += number_1[1] * number_2[0]
    return answer