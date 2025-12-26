import sys

if len(sys.argv) != 2:
    print("Нужен один файл")
    exit()
filename = sys.argv[1]
f = open(filename, 'r')
lines = f.readlines()
f.close()
nums = []
for line in lines:
    line = line.strip()
    if line:
        nums.append(int(line))
if len(nums) == 0:
    print(0)
    exit()
sorted_nums = sorted(nums)
n = len(sorted_nums)
if n % 2 == 1:
    med = sorted_nums[n//2]
else:
    med = sorted_nums[n//2 - 1]
total = 0
for num in nums:
    total += abs(num - med)
if total <= 20:
    print(total)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу.")