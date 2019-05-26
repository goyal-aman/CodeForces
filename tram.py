capacity = temp = 0
for _ in [0]*int(input()):
    temp-=eval(input().replace(' ','-'))
    capacity = max(temp, capacity)
print(capacity)