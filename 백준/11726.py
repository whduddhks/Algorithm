import sys
sys.setrecursionlimit(10**6)

def factorial(n):
    if(n == 0):
        return 1
    return n*factorial(n-1)

def Homogeneous(n, r):
    if(r == 0):
        return 1
    if(n == 0):
        return 1
    return factorial(n+r-1)/factorial(r)/factorial(n-1)


n = int(input())
answer = 0
one = n//2
two = n%2
while(one >= 0):
    answer += Homogeneous(one+1, two)
    one -= 1
    two += 2
print(answer%10007)