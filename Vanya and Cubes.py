n = int(input())
temp = 2
while n>=sum(range(1,temp)):

    n -= sum(range(1,temp))
    temp +=1
print(temp-2)
