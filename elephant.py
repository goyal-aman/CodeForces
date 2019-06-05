s = int(input())
step = 0
l = [5,4,3,2,1]
run = True
while s>0:
    if s >= 5:
        step +=1
        s-=5
    elif s >= 4:
        step += 1
        s -= 4
    elif s >= 3:
        step += 1
        s -= 3
    elif s >= 2:
        step += 1
        s -= 2
    elif s >= 1:
        step += 1
        s -= 1

print(step)