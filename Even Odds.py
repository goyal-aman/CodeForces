n, k = map(int, input().split())
odd = int(-(-n//2) if n%2 else n/2)
print([2*(k-odd) , 2*k-1][k<=odd])

# for i in range(1,n+1):
#     if i%2:
#         output.append(i)
# for i in range(1,n+1):
#     if not i%2:
#         output.append(i)
# print(output)
# print(output[k-1])
