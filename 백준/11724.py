import sys


def connect_cal(i, point, connect_list, visit):
    now_visit = []
    now_connect = point[i]
    now_visit.append(i+1)
    while now_visit != now_connect:
        new_connect = now_connect
        for num in now_connect:
            new_connect += point[num-1]
            now_visit.append(num)
            new_connect = list(set(new_connect))
            now_visit = list(set(now_visit))
        now_connect = new_connect
    connect_list.append(now_connect)
    visit += now_visit
    return connect_list, visit


point_num, line_num = map(int, input().split())
point = [[] for i in range(point_num)]

for line in sys.stdin.readlines():
    point1, point2 = map(int, line.split())
    point[point1-1].append(point2)
    point[point2-1].append(point1)

visit = []
connect_list = []

for i in range(len(point)):
    if i+1 not in visit:
        connect_list, visit = connect_cal(i, point, connect_list, visit)
    else:
        continue

print(len(connect_list))