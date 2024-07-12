import csv
import re
from pprint import pprint
from collections import defaultdict

# читаем книгу CSV
with open("Regulars/phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# форматирование ФИО
def normalize_names(contact):
    full_name = " ".join(contact[:3]).split()
    while len(full_name) < 3:
        full_name.append('')
    contact[:3] = full_name
    return contact


contacts_list = [normalize_names(contact) for contact in contacts_list]

# чистим телефонные номера
pattern = r"(\+7|8)?\s*\((\d+)\)\s*(\d+)[\s-]*(\d+)[\s-]*(\d+)"
substr = r"+7(\2)\3-\4-\5"

pattern_comp = re.compile(pattern)
print(type(pattern_comp))


def normalize_phone(contact):
    contact[-2] = re.sub(pattern, substr, contact[-2])
    return contact


contacts_list = [normalize_phone(contact) for contact in contacts_list]

# объединяем дублирующиеся записи
contacts_dict = defaultdict(lambda: ["", "", "", "", "", "", ""])

for contact in contacts_list:
    key = (contact[0], contact[1])
    existing_contact = contacts_dict[key]
    for i in range(7):
        if not existing_contact[i] and contact[i]:
            existing_contact[i] = contact[i]

contacts_list = list(contacts_dict.values())

# выводим
for contact in contacts_list:
    pprint(contact)
    print()

# сохраняем
with open("Regulars/phonebook_1.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
