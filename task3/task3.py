import argparse
import json
import os

def load_json_file(path):
    while True:
        if not os.path.exists(path):
            print(f"Файл '{path}' не найден, попробуйте снова")
            path = input("Введите путь к файлу: ")
            continue
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Файл '{path}' содержит некорректный JSON, попробуйте другой")
            path = input("Введите путь к файлу: ")
        except Exception as e:
            print(f"Ошибка при открытии файла '{path}': {e}")
            path = input("Введите путь к файлу: ")
def fill(tests, values_map):
    for test in tests:
        if 'id' in test and test['id'] in values_map:
            test['value'] = values_map[test['id']]
        if 'values' in test:
            fill(test['values'], values_map)
parser = argparse.ArgumentParser(description="Заполнение JSON-тестов значениями")
parser.add_argument("values_file", nargs='?', help="Файл со значениями")
parser.add_argument("tests_file", nargs='?', help="Файл с тестами")
parser.add_argument("report_file", nargs='?', help="Файл для записи отчёта")
args = parser.parse_args()
values_file = args.values_file or input("Введите путь к файлу со значениями: ")
tests_file = args.tests_file or input("Введите путь к файлу с тестами: ")
report_file = args.report_file or input("Введите путь к файлу для записи отчёта: ")
values_data = load_json_file(values_file)
tests_data = load_json_file(tests_file)
values_map = {item['id']: item['value'] for item in values_data.get("values", [])}
tests = tests_data.get("tests", [])
fill(tests, values_map)
try:
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(tests_data, f, indent=2, ensure_ascii=False)
    print(f"Результат успешно записан в '{report_file}'")
except Exception as e:
    print(f"Не удалось записать файл '{report_file}': {e}")
