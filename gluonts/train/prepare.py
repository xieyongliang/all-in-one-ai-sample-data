import sys
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

path = sys.argv[1]
file = open(path, 'r')
minstart = None
maxend = None
lines = file.readlines()
for line in lines:
    line = json.loads(line)
    start = line['start']
    target = line['target']
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    if(minstart == None):
        minstart = start
    else:
        minstart = min(minstart, start)
    end = start + relativedelta(months=len(target))
    if(maxend == None):
        maxend = end
    else:
        maxend = max(maxend, end)
    
print('start:', start)
print('end:', end)
    
