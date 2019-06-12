n = int(input())
print(*[[9,n-9],[8,n-8]][not n&1])

# def CheckPrime(n):
#     i, count = 1,0
#     while i<= n:
#         count += 1 if n%i==0 else 0
#         i+=1
#     return count<3
#
# n = int(input())
# while True:
#     temp = 4
#     while temp < n:
#         # print(CheckPrime(temp), CheckPrime(n-temp))
#         if  (not CheckPrime(temp) and not CheckPrime(n-temp)):
#             print(temp, n-temp)
#             exit()
#         temp +=1