import sys
import uuid

path = sys.argv[1]
file = open(path, 'r')
lines = file.readlines()
for line in lines:
    pos = line.rfind('####')
    text = line[0: pos]
    tmp_file = open('{0}.txt'.format(str(uuid.uuid4())),'w')
    tmp_file.write(text)
    tmp_file.close()
