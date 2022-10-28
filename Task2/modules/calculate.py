from modules.calculations.dif import dif
from modules.calculations.div import div
from modules.calculations.mult import mult
from modules.calculations.sum import sum

def calculate(first_number, second_number, operation):
        if operation == "+":
            return sum(first_number, second_number)
        elif operation == "-":
            return dif(first_number, second_number)
        elif operation == "*":
            return mult(first_number, second_number)
        elif operation == "/":
            return div(first_number, second_number)
