import json
import os
import re

import chardet


def save(str_list: list):
    with open('comments.json', 'w', encoding='utf-8') as file:
        json.dump(str_list, file, ensure_ascii=False, indent=4)


def load() -> []:
    with open('comments.json', 'r', encoding='utf-8') as file:
        lst = json.load(file)
    return lst


def get_comments(filename):
    with open(filename, 'rb') as fl:
        raw_data = fl.read()
        encoding = chardet.detect(raw_data)['encoding']

    with open(filename, 'r', encoding=encoding) as fl:
        raw_data = fl.read()

    lines = [line.strip() for line in raw_data.split('\n') if line.strip()]

    filters = [
        r'^\d+(\.\d+)?[Kk]?$',
        r'^Reply$',
        r'^\d+\sreplies$',
        r'^\d+\s+reply$',
        r'^@\w+',
        r'^\d+\s+(year|month|week|day|hour|minute)s?\s+ago$',
        r'^\d+\s+reply,\s+\d+\s+(year|month|week|day|hour|minute)s?\s+ago$',
        r'^\d+\s+(year|month|week|day|hour|minute)s?\s+ago\s+\(edited\)$',
    ]

    filter_regex = re.compile('|'.join(filters))

    comments = []

    for line in lines:
        if not filter_regex.search(line):
            if (len(line) > 30):
                comments.append(line)

    return comments


files = os.listdir('raw')
file_list = [file for file in files if os.path.isfile(os.path.join('raw', file))]

data = []

for f in files:
    print(f)
    data.extend(get_comments(f'raw/{f}'))

save(data)
dt = load()

print(len(dt))
print(len(data))
