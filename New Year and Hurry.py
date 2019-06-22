n,k = map(int, input().split())
while n*(n+1)*5//2 > 240-k:
    n-=1
print(n)

# n,k = map(int, input().split())
# remaining_time = 4*60 - k
# i = 0
# while remaining_time >= 5*(i+1) and i<n:
#     i += 1
#     remaining_time -= 5*i
# print(i)