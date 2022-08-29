import sys
import json
import uuid

path = sys.argv[1]
field = sys.argv[2]
file = open(path, 'r')
lines = file.readlines()
for line in lines:
    data = json.loads(line)
    text = data[field]
    tmp_file = open('{0}.txt'.format(str(uuid.uuid4())),'w')
    tmp_file.write(text)
    tmp_file.close()
