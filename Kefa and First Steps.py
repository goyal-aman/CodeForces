s = int(input())
a = list(map(int, input().split()))
c,d = 0,0
for i in range(s-1):
    c = c+1 if a[i] <= a[i+1] else 0
    d = max(c,d)
print(d+1)