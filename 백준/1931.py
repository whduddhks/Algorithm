import sys


N = int(input())
time_dic = {}
for line in sys.stdin.readlines():
    line = line.split()
    if int(line[0]) in time_dic:
        time_dic[int(line[0])].append(int(line[1]))
    else:
        time_dic[int(line[0])] = [int(line[1])]

time_dic = dict(sorted(time_dic.items()))

last_session = 0
for key in time_dic.keys():
    sorted_value = time_dic[key]
    sorted_value.sort()
    time_dic[key] = sorted_value
    if key > last_session:
        last_session = key

max_session_num = 0
for i in range(0,last_session+1):
    start_time = i
    session_num = 0
    while start_time <= last_session:
        if start_time in time_dic:
            for j in time_dic[start_time]:
                if j >= start_time:
                    session_num += 1
                    start_time = j
                    break
        else:
            start_time += 1
    if max_session_num < session_num:
        max_session_num = session_num

print(max_session_num)

