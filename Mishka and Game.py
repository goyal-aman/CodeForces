m,c = 0,0
for _ in range(int(input())):
    t1,t2 = map(int, input().split())
    if t1 > t2:
        m +=1
    elif t1<t2:
        c +=1

print(['Mishka', 'Chris'][m<c] if (m != c)  else 'Friendship is magic!^^')