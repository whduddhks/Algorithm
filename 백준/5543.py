import sys
num = 0
burger = 3000
beverage = 3000
for line in sys.stdin:
    line = int(line)
    if(num < 3):
        if(line < burger):
            burger = line
        num += 1
    else:
        if(line < beverage):
            beverage = line
print(burger + beverage - 50)