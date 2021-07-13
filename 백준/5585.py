money = 1000 - int(input())
answer = 0
moneylist = [500, 100, 50, 10, 5, 1]
for i in moneylist:
    if(money//i >= 1):
        answer += money//i
        money %= i
print(answer)
