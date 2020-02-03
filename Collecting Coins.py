t = int(input())
for _ in range(t):
    a,b,c,n = map(int, input().split())
    li = sorted([a,b,c], reverse=True)
    # print(li)
    n -= (2*li[0] - li[1] - li[2])
    if n>=0 and n%3==0:
        print("YES")
    else:
        print("NO")

