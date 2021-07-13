import sys
N, score, rank = map(int, input().split())
front = 0
same = 0
back = 0
for num in sys.stdin.readline().split():
    num = int(num)
    if(score < num):
        front += 1
    elif(score == num):
        same += 1
    else:
        back += 1
if(front + same < rank):
    print(front + 1)
else:
    print(-1)