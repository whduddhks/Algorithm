def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant, completion)
    answer = participant[-1]
    for num in range(len(completion)):
        if(completion[num] != participant[num]):
            answer = participant[num]
    return answer

participant = ['leo', 'kiki', 'eden', 'leo']
completion = ['eden', 'kiki', 'leo']
print(solution(participant, completion))
