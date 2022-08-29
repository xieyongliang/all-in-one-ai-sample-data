import sys
import uuid
import json

path = sys.argv[1]
file = open(path, 'r')
lines = file.readlines()
dict = {}
i = 0
max_entries = 100

labels = [
    '民生',
    '文化',
    '娱乐',
    '体育',
    '财经',
    '房产',
    '汽车',
    '教育',
    '科技',
    '军事',
    '旅游',
    '国际',
    '证券',
    '农业',
    '电竞'
]

for line in lines:
    items = line.split('_!_')
    category = items[1]
    title = items[3]
    if(category not in dict):
        dict[category] = []
    if(len(dict[category]) < max_entries):
        dict[category].append(title)
for category in dict:
    for title in dict[category]:
        tmp_file = open('{0}.json'.format(str(uuid.uuid4())), 'w')
        tmp_file.write(
            json.dumps(
                {
                    "data": title,
                    "labels": labels
                },
                ensure_ascii = False
            )
        )
        tmp_file.close()
    