import sys
count = int(input())
numlist = []
for line in sys.stdin:
    numlist.append(int(line))
num = 0
for i in range(len(numlist)-1):
    if (numlist[i] > numlist[i+1]):
        num += 1

print(num+1)