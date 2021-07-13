N, K = map(int, input().split())
cir_list = list(range(0, N+1))
per_list = []
now_per = 0
print(cir_list)
while len(cir_list) != 1:
    now_per = (now_per + K)%(N+1)
    if now_per == 0:
        now_per = 1
    print(now_per)
    per_list.append(cir_list[now_per])
    del cir_list[now_per]
    print(per_list)
    print(cir_list)
print(per_list)