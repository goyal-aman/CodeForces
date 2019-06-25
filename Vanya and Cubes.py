n = int(input())
i = 1
total_cube = 0
while total_cube <= n:
    total_cube += (i*(i+1))//2
    i+=1
print(i-2)

# n = int(input())
# temp = 2
# while n>=sum(range(1,temp)):
#
#     n -= sum(range(1,temp))
#     temp +=1
# print(temp-2)
