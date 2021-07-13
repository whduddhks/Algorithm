import sys


A, B = map(int, input().split())
length = int(input())
num_list = sys.stdin.readline().split()

number = 0
loc = 0
for i in range(length-1, -1, -1):
    number += int(num_list[i])*(A**loc)
    loc += 1

answer_list = []
while(number >= B):
    answer_list.append(number%B)
    number //= B

answer_list.append(number)
for i in range(len(answer_list)-1, -1, -1):
    print(answer_list[i], end=" ")