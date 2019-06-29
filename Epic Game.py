from math import gcd
a,b,n = map(int, input().split())
turn = 1
while n>0:
    if turn&1:
        n-=gcd(n,a)
    else:
        n-=gcd(b,n)
    turn+=1
print(1 if turn&1 else 0)