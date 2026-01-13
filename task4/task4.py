import sys
import os

if len(sys.argv) != 2:
    print("Нужен один файл c числами")
    exit()

filename = sys.argv[1]
try:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл '{filename}' не найден")
    with open(filename, 'r') as f:
        lines = f.readlines()
except Exception as e:
    print(f"Не удалось открыть файл '{filename}': {e}")
    exit()
nums = []
for line in lines:
    line = line.strip()
    if line:
        try:
            nums.append(int(line))
        except ValueError:
            print(f"Ошибка: '{line}' не является целым числом")
            exit()
if len(nums) == 0:
    print(0)
    exit()
sorted_nums = sorted(nums)
n = len(sorted_nums)
if n % 2 == 1:
    med = sorted_nums[n // 2]
else:
    med = sorted_nums[n // 2 - 1]
total = sum(abs(num - med) for num in nums)
if total <= 20:
    print(total)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу.")
