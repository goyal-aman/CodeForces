input()
s = list(map(int, input().split()))
recruit = 0
untreated = 0
for i in s:
    if i < 0 and recruit==0:
        untreated+=1
    else:
        recruit +=i
print(untreated)
