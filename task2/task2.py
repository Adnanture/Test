f1 = open("circle.txt", "r")
line1 = f1.readline()
line2 = f1.readline()
f1.close()
cx, cy = map(float, line1.split())
a, b = map(float, line2.split())
f2 = open("dot.txt", "r")
lines = f2.readlines()
f2.close()
for line in lines:
    line = line.strip()
    if line == "":
        continue
    x, y = map(float, line.split())
    value = ((x - cx) ** 2) / (a ** 2) + ((y - cy) ** 2) / (b ** 2)
    if abs(value - 1.0) < 1e-9:
        print(0)
    elif value < 1.0:
        print(1)
    else:
        print(2)