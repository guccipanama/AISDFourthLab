# python validator.py input.txt output.txt

import json
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()


class validator:
    def __init__(self):
        pass

    def check_telephone(telephone) -> bool:  # тайпхинтинг
        if type(telephone) != str:
            return False
        pattern = '\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$'
        if re.match(pattern, telephone):
            return True
        return False

    def check_height(height: str) -> bool:
        if type(height) != str:
            return False
        pattern = '[12]\.\d'
        if re.match(pattern, height):
            return True
        return False

    def check_inn(inn: str) -> bool:
        if type(inn) != str:
            return False
        if len(inn) == 12:
            return True
        return False

    def check_passport(number: int) -> bool:
        if len(str(number)) == 6:
            return True
        return False

    def check_occupation(university: str) -> bool:
        if type(university) != str:
            return False
        return True

    def check_age(age: int) -> bool:
        if type(age) != int:
            return False
        if age < 14 or age > 60:
            return False
        return True

    def check_views(views: str) -> bool:
        if type(views) != str:
            return False
        return True

    def check_worldview(worldview: str) -> bool:
        if type(worldview) != str:
            return False
        return True

    def check_address(address: str) -> bool:
        if type(address) == str:
            pattern = '[а-яА-Я.\s\d-]+\s+[0-9]+$'
            if re.match(pattern, address):
                return True
        return False


data = json.load(open(args.input, encoding='windows-1251'))

valid_data = list()
telephone = 0
height = 0
inn = 0
passport_number = 0
occupation = 0
age = 0
political_views = 0
worldview = 0
address = 0

for person in data:
    temp = True
    if not validator.check_telephone(person["telephone"]):
        telephone += 1
        temp = False
    if not validator.check_height(person["height"]):
        height += 1
        temp = False
    if not validator.check_inn(person['inn']):
        inn += 1
        temp = False
    if not validator.check_passport(person['passport_number']):
        passport_number += 1
        temp = False
    if not validator.check_occupation(person["occupation"]):
        occupation += 1
        temp = False
    if not validator.check_age(person['age']):
        age += 1
        temp = False
    if not validator.check_views(person['political_views']):
        political_views += 1
        temp = False
    if not validator.check_worldview(person['worldview']):
        worldview += 1
        temp = False
    if not validator.check_address(person["address"]):
        address += 1
        temp = False
    if temp:
        valid_data.append(person)

out_put = open(args.output, 'w', encoding='utf-8')
data_for_output = json.dumps(valid_data, ensure_ascii=False, indent=4)
out_put.write(data_for_output)
out_put.close()

print()
print(f'Всего {len(data)} записей')
print(f'{len(valid_data)} валидных записей')
print(f'{len(data) - len(valid_data)} невалидных записей')
print()
print(f'Число невалидных номеров телефона:  {telephone}')
print(f'Число невалидных ростов: {height}')
print(f'Число невалидных ИНН: {inn}')
print(f'Число невалидных номеров паспорта: {passport_number}')
print(f'Число невалидных занятостей {occupation}')
print(f'Число невалидных возрастов: {age}')
print(f'Число невалидных политических взглядов: {political_views}')
print(f'Число невалидных мировоззрений: {worldview}')
print(f'Число невалидных адрессов: {address}')
