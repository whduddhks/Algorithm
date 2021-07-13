A, B = map(int, input().split())

gcd_A = A
gcd_B = B
while True:
    if gcd_A > gcd_B:
        if gcd_A % gcd_B == 0:
            gcd = gcd_B
            break
        else:
            gcd_A %= gcd_B
    else:
        if gcd_B % gcd_A == 0:
            gcd = gcd_A
            break
        else:
            gcd_B %= gcd_A

print(gcd)
     
lcm_A = A
lcm_B = B
while lcm_A != lcm_B:
    if lcm_A > lcm_B:
        lcm_B += B
    else:
        lcm_A += A

print(lcm_A)