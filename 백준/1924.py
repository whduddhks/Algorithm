x, y = map(int, input().split())
datelist = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
numlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num = y
for i in range(x-1):
    num += numlist[i]

print(datelist[num%7])