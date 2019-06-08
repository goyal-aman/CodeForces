# n -
# m |
n,m = map(int, input().split())
turn = 0
while n and m:
    turn +=1 #odd turn : akshat
    n-=1
    m-=1
print(['Akshat','Malvika'][turn%2==0])