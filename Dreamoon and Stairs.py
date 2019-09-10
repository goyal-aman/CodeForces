n,m = map(int, input().split())
t = (n//2) - (n//2)%m + m

print((-(-n//2) if -(-n//2)%m==0 else t) if n>=m else -1)