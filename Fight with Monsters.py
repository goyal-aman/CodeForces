n, a, b, k = map(int, input().split())
# li = list(map(int, input().split()))
li = []
ans = 0
for hp in map(int, input().split()):

    # skipping to the final battle 
    # for each moster
    hp = hp%(a+b) 
    
    # if hp at the beggining of final battle
    # is zero, then opponent has won,
    hp = a+b if hp==0 else hp
    
    # calculating no of times special power
    # is required for me to kill the monster
    hp = -(-hp//a)-1
    li.append(hp)    


li.sort()

for i in li:
    k-=i
    if k<0:
        break
    ans += 1
print(ans)
