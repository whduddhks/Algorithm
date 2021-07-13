def longestPalindrome(s):
    len_s = len(s)                           # s의 길이 저장 
    min = -1
    max = -1                                 # max는 -1로 시작
    while max == -1:                         # max의 값이 바뀌면 반복문 종료
        print(len_s)
        start = 0                            # substring의 시작 부분 지정
        last = len_s                         # substring의 마지막 부분 지정
        while last != len(s) + 1:            # last가 s의 마지막 부분을 지나친 경우 반복문 종료
            print(s[start:last])
            find = 1
            for match in range((last - start)//2):
                if s[start + match] != s[last - match - 1]:
                    find = 0
                    break   
            if find == 1:
                min = start
                max = last
                break
            else:
                start += 1                        # palindromic한 substring이 없는 경우 시작 부분 1 증가
                last += 1                         # 마지막 부분 1 증가
        len_s -= 1                            # 길이 1 줄이기
        if len_s == 0:                        # 만약 2개의 palindromic한 substring까지 없다면 
            max = 0                           # max는 0으로 값 반환
    print(min, max)
    return s[min:max]


print(longestPalindrome("cbbd"))

