import sys
import json

if len(sys.argv) != 4:
    print("Неверное количество аргументов")
    exit()
values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

f = open(values_file, 'r', encoding='utf-8')
values_data = json.load(f)
f.close()
values_map = {}
for item in values_data["values"]:
    values_map[item['id']] = item['value']
f = open(tests_file, 'r', encoding='utf-8')
data = json.load(f)
f.close()
tests = data["tests"]
def fill(tests):
    for test in tests:
        if 'id' in test and test['id'] in values_map:
            test['value'] = values_map[test['id']]
        if 'values' in test:
            fill(test['values'])
fill(tests)
f = open(report_file, 'w', encoding='utf-8')
json.dump(data, f, indent=2, ensure_ascii=False)
