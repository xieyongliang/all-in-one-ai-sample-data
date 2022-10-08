import os
import json
import shutil

if not os.path.exists('test'):
    os.makedirs('test')

test = json.loads(open('meta/test.json', 'r').read())

for clazz in test.keys():
    for file_path in test[clazz]:
        directory = file_path[0 : file_path.find('/')]
        if not os.path.exists('test/{0}'.format(directory)):
            os.makedirs('test/{0}'.format(directory))
        shutil.copyfile('images/{0}.jpg'.format(file_path), 'test/{0}.jpg'.format(file_path))

if not os.path.exists('train'):
    os.makedirs('train')

train = json.loads(open('meta/train.json', 'r').read())

for clazz in train.keys():
    for file_path in train[clazz]:
        directory = file_path[0 : file_path.find('/')]
        if not os.path.exists('train/{0}'.format(directory)):
            os.makedirs('train/{0}'.format(directory))
        shutil.copyfile('images/{0}.jpg'.format(file_path), 'train/{0}.jpg'.format(file_path))