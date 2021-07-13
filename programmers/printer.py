def solution(priorities, location):
    answer = 0
    while(location != -1):
        printing = True
        now = priorities.pop(0)
        for num in priorities:
            if(now < num):
                printing = False
                priorities.append(now)
                if(location == 0):
                    location = len(priorities) -1
                else:
                    location -= 1
                break
        if(printing == True):
            answer += 1
            if(location == 0):
                location = -1
            else:
                location -= 1
    return answer


priorities = [2,1,3,4]
location = 2
print(solution(priorities, location))

#max값을 미리 찾아놓은 다음 이와 같은지 다른지를 비교하여 알고리즘을 조금 더 줄일 수 있을듯