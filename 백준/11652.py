import sys
numnum = int(input())
numdic = {}
for line in sys.stdin:
    line = int(line)
    if( line in numdic ):
        numdic[line] += 1
    else:
        numdic[line] = 1

num = 0
count = 0
for item in list(numdic.keys()):
    if( numdic.get(item) > count ):
        count = numdic.get(item)
        num = item
    elif(numdic.get(item) == count):
        if(num > item):
            num = item
print(num)