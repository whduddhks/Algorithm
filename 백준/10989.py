import sys
numlist = []
count = int(input())
for line in sys.stdin:
    numlist.append(int(line))
numlist.sort()
for num in numlist:
    print(num)