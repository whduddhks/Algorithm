numlist = [0,0,0,0,0,0,0,0,0,0]
num = int(input())
while (num > 0):
    numlist[num%10] += 1
    num //= 10
print('9'*numlist[9] + '8'*numlist[8] + '7'*numlist[7] + '6'*numlist[6] + '5'*numlist[5] + '4'*numlist[4] + '3'*numlist[3] + '2'*numlist[2] + '1'*numlist[1] + '0'*numlist[0])