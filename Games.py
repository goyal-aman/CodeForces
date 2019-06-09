n = int(input())
s=[]
count = 0
for _ in range(n):
    s.append(list(map(int, input().split())))
for i in range(n):
    t = s[i][0]
    for j in range(n):
        p = s[j][1]
        if t == p:
            count +=1
print(count)