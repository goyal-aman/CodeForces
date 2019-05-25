num = input()
stone = input()
print( sum(a==b for a,b in zip(stone[1:],stone)) )