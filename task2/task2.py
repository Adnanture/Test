import sys

args = sys.argv[1:]
while True:
    try:
        if len(args) >= 4:
            try:
                cx, cy, a, b = map(float, args[:4])
                point_args = args[4:]
                if len(point_args) == 0 or len(point_args) % 2 != 0:
                    raise ValueError("Ошибка: координаты точек заданы некорректно")
                points = []
                for i in range(0, len(point_args), 2):
                    x, y = float(point_args[i]), float(point_args[i+1])
                    points.append((x, y))
                break
            except ValueError as ve:
                print("Данные аргументов командной строки некорректны:", ve)
        ellipse_input = input("Введите cx cy a b через пробел: ").split()
        if len(ellipse_input) != 4:
            print("Ошибка: нужно ввести ровно 4 числа для эллипса")
            continue
        try:
            cx, cy, a, b = map(float, ellipse_input)
        except ValueError:
            print("Ошибка: координаты и радиусы должны быть числами")
            continue
        points = []
        while True:
            line = input("Введите координаты точки x y (пустая строка — конец): ").strip()
            if line == "":
                break
            parts = line.split()
            if len(parts) != 2:
                print("Ошибка: нужно ввести ровно 2 числа для одной точки")
                continue
            try:
                x, y = map(float, parts)
                points.append((x, y))
            except ValueError:
                print("Ошибка: координаты должны быть числами")
        if not points:
            print("Ошибка: не введено ни одной точки")
            continue
        break
    except Exception as e:
        print("Произошла непредвиденная ошибка:", e)
for x, y in points:
    v = ((x - cx) ** 2) / (a ** 2) + ((y - cy) ** 2) / (b ** 2)
    if abs(v - 1.0) < 1e-9:
        print(0)
    elif v < 1.0:
        print(1)
    else:
        print(2)
