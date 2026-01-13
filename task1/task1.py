import sys

def build_massiv(n, m):
    massiv = []
    start = 0
    while True:
        massiv.append(str(start + 1))
        start = (start + m - 1) % n
        if start == 0:
            break
    return ''.join(massiv)
args = sys.argv[1:]
while True:
    try:
        if len(args) == 1:
            filename = args[0]
            try:
                f = open(filename, 'r')
                data = f.read().split()
                f.close()
                if len(data) != 4:
                    raise ValueError
                n1, m1, n2, m2 = map(int, data)
                break
            except FileNotFoundError:
                print(f"Файл {filename} не найден, вводим числа вручную")
            except ValueError:
                print(f"Данные файла {filename} некорректны, вводим числа вручную")
        elif len(args) == 4:
            try:
                n1, m1, n2, m2 = map(int, args)
                break
            except ValueError:
                print("Ошибка: аргументы должны быть целыми числами")
        while True:
            user_input = input("Введите n1 m1 n2 m2 через пробел: ").split()
            if len(user_input) != 4:
                print("Ошибка: нужно ввести ровно 4 числа")
                continue
            try:
                n1, m1, n2, m2 = map(int, user_input)
                break
            except ValueError:
                print("Ошибка: все значения должны быть целыми числами")
        break
    except Exception as e:
        print("Произошла ошибка:", e)
result = build_massiv(n1, m1) + build_massiv(n2, m2)
print("Результат:", result)
