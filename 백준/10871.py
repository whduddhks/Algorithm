import sys
N, X = map(int, input().split())
Nlist = list(map(int, sys.stdin.readline().split()))
answer = []
for i in Nlist:
    if(i < X):
        answer.append(i)
for i in answer:
    print(i, end=" ")