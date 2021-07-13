date = int(input())
carlist = list(map(int, input().split()))
answer = 0
for i in carlist:
    if(i == date):
        answer += 1
print(answer)