import re

pattern = re.compile("^%ERROR")

for i, line in enumerate(open('test.txt')):
    for match in re.finditer(pattern, line):
        print ('Found on line %s: %s' % (i+1, match.group()))
        