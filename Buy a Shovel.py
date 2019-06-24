cost, r = map(int, input().split())
i = 1
while cost*i%10!=0 and cost*i%10!=r:
    i+=1
print(i)