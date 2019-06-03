#k the cost of the first banana
# n initial number of dollars the soldier
#w number of bananas he wants
k, n, w = map(int, input().split())
count = 0
for i in range(1,w+1):
    count += i*k
print([0,count - n][count > n])