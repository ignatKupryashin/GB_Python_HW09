# 3. Создайте программу для игры в ""Крестики-нолики"".
import math
import emoji


def emoji_change(string):
    if string == "X":
        string = emoji.emojize(":cross_mark:")
    elif string == "O":
        string = emoji.emojize(":hollow_red_circle:")
    return string

def print_field(array):
    print("------------")
    for i in range(0, len(array), 3):
        print(f" {array[i]} | {array[i+1]} | {array[i+2]} ")
        print("------------")


def change_players(player):
    if player == emoji.emojize(":cross_mark:"):
        player = emoji.emojize(":hollow_red_circle:")
    else:
        player = emoji.emojize(":cross_mark:")
    return player


def move(player, field):
    point = input(f"Игрок {player}, Введите номер поля, в который вы хотите поставить символ: ")
    if point.isdigit():
        if 0 < int(point) < 10:
            point = int(point) - 1
            if field[point] != emoji.emojize(":cross_mark:") and field[point] != emoji.emojize(":hollow_red_circle:"):
                return point
            else:
                print("Указанное поле занаято.")
                return move(player, field)
        else:
            print("Такого поля не существует")
            move(player, field)
    else:
        print("Введите поле цифрой от 1 до 9")
        move(player, field)

def check_victory(field, point):
        check_point = math.floor(point / 3)
        if field[check_point] == field[check_point + 1] == field[check_point + 2]:
            return True
        elif field[point] == field [point - 3] == field[point - 6]:
            return True
        elif point in (0, 2, 4, 6, 8):
                if field[0] == field[4] == field[8] or field[2] == field [4] == field[6]:
                    return True
        else:
            return False


field = []
for i in range (0,9):
    field.append(i+1)

player = emoji.emojize(":cross_mark:")
print_field(field)
win = False
for i in range(9):
    point = move(player, field)
    field[int(point)] = player
    print_field(field)
    if check_victory(field, point) == True:
        win = True
        break
    player = change_players(player)

if win:
    print()
    print(emoji.emojize(":thumbs_up:"))
    print(f"Победил игрок {player}")
else:
    print()
    print("Ничья!")


