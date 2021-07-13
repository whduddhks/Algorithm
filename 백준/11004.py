import sys
num, K = map(int, input().split())
numlist = []
for line in sys.stdin.readline().split():
    line = int(line)
    numlist.append(line)
numlist.sort()
print(numlist[K-1])