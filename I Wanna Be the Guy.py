s = int(input())
x = set(map(int, input().split()[1::]))
y = set(map(int, input().split()[1::]))
x |= y
l = set()
for i in range(1,s+1):
    l.add(i)
print(['Oh, my keyboard!','I become the guy.'][l == x])
