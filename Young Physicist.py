x,y,z = 0,0,0
for _ in range(int(input())):
    a,b,c = map(int, input().split())
    x +=a
    y+=b
    z+=c
print(['NO','YES'][ x==0 and y==0 and z ==0])