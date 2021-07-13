A = int(input())
B = int(input())
C = int(input())
numlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
answer = A*B*C
while(answer != 0):
    i = answer%10
    numlist[i] += 1
    answer //= 10

for i in numlist:
    print(i)