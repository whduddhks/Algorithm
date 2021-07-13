import sys

N = int(input())
num_list = sys.stdin.readline().split()

max_increase = 0
for i in range(N):
    now_num = num_list[i]
    increase = 1
    for j in range(i+1, N):
        if num_list[j] > now_num:
            now_num = num_list[j]
            increase += 1
    if max_increase < increase:
        max_increase = increase

print(max_increase)