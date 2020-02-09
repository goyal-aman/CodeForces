t = int(input())
for _ in range(t):
    li = [0,0]
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        li[i%2]+=1
    # print(f"li: {li}")
    
    # if there is even a single odd, output is "YES"
    if li[1]>0 and li[0]>0:
        print("YES")
    
    #only odd numbers
    elif li[1]>0 and li[0]==0:
        if li[1]%2==0:
            print("NO")
        else:
            print("YES")

    else:
        print("NO")

    # 
    # when odd sum is not possible??
    # 1. no odd
    # 2. all even and even number of odds
    # 
'''
if (    sare even number h
    ya
    odd number even times h
    ): 'no'
else:
    'yes'

'''