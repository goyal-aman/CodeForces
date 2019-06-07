n = int (input())
s = list(map(int, input().split()))
for i in range(n-1, 0 , -1):
    for j in range(i):
        if s[j] > s[j+1]:
            s[j], s[j+1] = s[j+1], s[j]
print(*s)