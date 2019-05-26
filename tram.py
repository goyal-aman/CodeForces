a = int(input())
capacity, temp = 0, 0
temp2 = 0
for _ in range(a):
    s = list(map(int, input().split()))
    temp += s[1] - s[0]
    if temp > capacity:
        capacity = temp
print(capacity)