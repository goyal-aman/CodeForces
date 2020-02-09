t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    x=y=0
    visited = {(x,y):0}
    min_len = n+1
    l,r = -1,n
    
    i=1
    for j in range(n):
        if s[j]=='L':
            x-=1
        elif s[j]=='R':
            x+=1
        elif s[j]=='U':
            y+=1
        else:
            y-=1
        
        if (x,y) in visited:
            if i-visited[(x,y)] < min_len:
                l = visited[(x,y)]
                r = i             
                min_len  = i-visited[(x,y)]   
        visited[(x,y)]=i
        i+=1

    if min_len>n:
        print(-1)
    else:
        print(l+1, r)