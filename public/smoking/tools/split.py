from sklearn.model_selection import train_test_split
import sklearn
import shutil

train, test = sklearn.model_selection.train_test_split(range(0, 2482), test_size=0.2, train_size=0.8, random_state=None, shuffle=True, stratify=None)

print(len(train))
print(len(test))

file = open('trainval.txt')
lines = file.readlines()
for i in range(0, len(lines)):
    if(i in test):
        shutil.move('images/train/{0}'.format(lines[i][0:-1] + '.jpg'), 'images/val/{0}'.format(lines[i][0:-1] + '.jpg'))
        shutil.move('labels/train/{0}'.format(lines[i][0:-1] + '.txt'), 'labels/val/{0}'.format(lines[i][0:-1] + '.txt'))