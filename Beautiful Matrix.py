i = 1
while i < 6:
    a = list(map(int, input().split()))
    if 1 in a:
        c = a.index(1) + 1
        break
    i+=1
print(abs(3-i) + abs(3-c))

# also works but cannot figure our how
#l=[2,1,0,1,2]
#for i in l:
# s=input()
# if"1"in s:print(i+l[s.find("1")//2])

jljj