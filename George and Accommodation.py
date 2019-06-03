n = int(input())
avail = 0
for _ in range(n):
    p, q = map(int, input().split())
    if q - p >= 2:
        avail +=1
print(avail)