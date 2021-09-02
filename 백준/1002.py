t = int(input())
for case in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    short, long = (r1, r2) if r1 < r2 else (r2, r1)
    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1+r2 < dis or dis+short < long:
            print(0)
        elif dis < r1+r2 and short+dis > long:
            print(2)
        else:
            print(1)

'''
두개의 원이 두 점에서 만나는 경우(elif절)에는 and를 사용해야한다.
or를 사용하는 경우, 두개의 원이 한 점에서 만나는 경우와 
dis < r1+r2 조건에서 겹칠 수 있다
(예. 한 원이 다른 원 안에 있는 경우)
'''