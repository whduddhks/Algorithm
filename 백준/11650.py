t = int(input())
coord = []
for case in range(t):
    x, y = map(int, input().split())
    coord.append((x,y))
coord.sort(key=lambda x: (x[0], x[1]))
for coor in coord:
    print(coor[0], coor[1])