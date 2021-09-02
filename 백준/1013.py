import re
t = int(input())
for case in range(t):
    s = input()
    p = re.compile("(100+1+|01)+")
    m = p.fullmatch(s)
    if m:
        print("YES")
    else:
        print("NO")

'''
re.fullmatch와 re.match의 차이는 크다
match는 일부라도 매치가 된다면 값을 반환하지만
fullmatch는 전체가 매치가 되지 않는다면 값을 반환하지 않는다

만약 re.match를 사용하고 싶다면 if문에서 s와 m.group()을 비교하여 같은지 다른지 비교할 수 있다
하지만 입력 문자가 없다면 m.group()이 없이 none이 되기 때문에
Attribute Error가 나오게 된다

따라서 여러 조건이 필요한 re.match보다
re.fullmatch를 이용하여 한번에 비교할 수 있다.
'''
        