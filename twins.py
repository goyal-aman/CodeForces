s = int(input())
coin = sorted(list(map(int, input().split())))
a = n = 0
for i in range(s):
    if a <= sum(coin):
        a = coin.pop()
        n+=1
print(n)