import math

num = int(input())
sqrtsum = 0
while (num > 3 ):
    temp = int(math.sqrt(num))**2
    num -= temp
    sqrtsum += 1
sqrtsum += num
print(sqrtsum)

#12의 경우 9 + 1 + 1 + 1 보다 4 + 4 + 4 가 더 적음