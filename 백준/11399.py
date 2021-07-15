N = int(input())
time = 0
for num in sorted(map(int, input().split())):
    time += num*N
    N-=1
print(time)