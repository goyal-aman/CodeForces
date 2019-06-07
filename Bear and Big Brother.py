a,b = map(int, input().split())
i = 1
while i:
    a *= 3
    b *= 2
    if a > b:
        break
    i+=1
print(i)