num = int(input())
stone = input()
remove,i = 0,0
while i < num-1:
    if stone[i] ==  stone[i+1]:
        remove+=1
    i+=1
print(remove)