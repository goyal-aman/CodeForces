t = int(input())
for _ in range(t):
    n = int(input())
    li = []
    i = 2
        
    while i*i<n:
        if n%i==0:
            li.append(i)
            n/=i
        if len(li)==2: 
            break
        i+=1
    if len(li)!=2 or n in li:
        print('NO')
    else:
        print("YES")
        print(li[0],li[1], int(n))