n = int(input())
print(max(n,int(n[:-1]), int(n[:-2] + n[-1])))
