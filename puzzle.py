n,s = map(int, input().split())
p = sorted(list(map(int, input().split())))
print(min(j-i for i,j in zip(p,p[n-1:])))