import sys
answer = 0
for line in sys.stdin:
    line = int(line)
    if (line < 40):
        answer += 40
    else:
        answer += line
print(int(answer/5))