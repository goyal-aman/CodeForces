magnets = int(input())
group, temp = 0, 0
for _ in range(magnets):
    magnets = int(input())
    if magnets!=temp:
        group+=1
    temp = magnets
print(group)