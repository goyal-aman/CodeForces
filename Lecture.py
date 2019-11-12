n,m = map(int, input().split())
d={}
for _ in range(m):
    a,b =   input().split()
    d[a] = b if len(b)<len(a) else a
string = []
for word in input().split():
    string.append(d[word])
print(' '.join(string))