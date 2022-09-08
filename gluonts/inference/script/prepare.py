import sys
import uuid
import json

path = sys.argv[1]
file = open(path, 'r')
lines = file.readlines()
for line in lines:
    tmp_file = open('{0}.json'.format(str(uuid.uuid4())),'w')
    data = json.loads(line)
    data['freq'] = '1M'
    data['prediction_length'] = 24
    line = json.dumps(data)
    tmp_file.write(line)
    tmp_file.close()
