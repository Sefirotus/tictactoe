def hello_friends():
    print("-------------------")
    print("    Настоящий ад   ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print("   Формат ввода    ")
    print("  X - Номер строки ")
    print("  Y - Номер столбца")
    print("-------------------")
    print("-------------------")

hello_friends()
field = [[" "] * 3 for i in range (3)]



def show_field():
    print(f"* |0|1|2| ")
    for i in range (3):
        row = " ".join(field[i])
        print(f"{i}| {row}")

def ask():
    while True:
        step = input("ваш ход").split()

        if len(step) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = step
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y =int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Возможные значения 0 1 2")
            continue
        if field[x][y] != " ":
            print("Клетка занята")
            continue
        if field[x][y] == " ":
            print("развязка близка")
            return x, y

def check_win():
    win_setup = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for step in  win_setup:
        a = step[0]
        b = step[1]
        c = step[2]
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != " ":
            print(f"Олала, это же победа {field[a[0]][c[1]]}!")
            return True
    return False

turn = 0
while True:
    turn += 1

    show_field()

    if turn %2 == 1:
        print("ходит X\n"
              "-------")
    else:
        print("Ходит О\n"
              "-------")

    x, y = ask()

    if turn %2 == 1:
        field [x] [y] = "X"
    else:
        field [x] [y] = "O"
    if check_win():
        break
    if turn == 9:
        break
        print("Дроу")