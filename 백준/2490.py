import sys
answer = [0, 0, 0]
answerlist = ["D", "C", "B", "A", "E"]
for i in range(3):
    for line in sys.stdin.readline().split():
        line = int(line)
        answer[i] += line
for i in answer:
    print(answerlist[i])