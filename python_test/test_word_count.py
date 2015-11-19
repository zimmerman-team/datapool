import re
from collections import Counter
import csv

with open('/home/daan/zimmerman/projects/datapool/datapool/python_test/ccountryken-twitteraf2012.csv') as f:
    f.seek(0)         
    text = ''                                                                            
    reader = csv.reader(f, delimiter=',')
    rownum = 0
    for row in reader:
        if rownum == 0:
            
            rownum += 1
            continue
        text = text+' '+row[1]
        print row[1]
exit()
print 'before regular expression'
words = re.findall(r'\w+', text)
print 'before most common function call'
print(Counter(words).most_common(30))