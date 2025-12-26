def build_massiv(n, m):
    massiv = []
    start = 0
    while True:
        massiv.append(str(start + 1))
        start = (start + m - 1) % n
        if start == 0:
            break
    return ''.join(massiv)
user_input = input("введите n1 m1 n2 m2 через пробел: ")
n1, m1, n2, m2 = map(int, user_input.split())
result = build_massiv(n1, m1) + build_massiv(n2, m2)
print(result)