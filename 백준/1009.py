t = int(input())
for case in range(t):
    a, b = map(int, input().split())
    last = []
    num = a
    while True:
        if num%10 in last:
            break
        last.append(num%10)
        num *= a
    print(last[b%(len(last))-1] if last[b%(len(last))-1] != 0 else 10)    