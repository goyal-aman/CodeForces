a = list(map(int, input().split('+')))
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j], a[j + 1] = a[j+1], a[j]
        j+=1
    i+=1
#print('+'.join(str(x) for x in a))
print("+".join(sorted(input()[::2])))
