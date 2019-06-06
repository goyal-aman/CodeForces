*k, d= [int(input()) for _ in range(5)]
print(d- sum(all(i%ch for ch in k)for i in range(1, d+1)))


# k = int(input())
# l = int(input())
# m = int(input())
# n = int(input())
# d = int(input())
# list = ['*']*d
# storage = d
# input_vars = [k,l,m,n]
# for ch in input_vars:
#     for i in range(1,int(d//ch)+1):
#         list[(i*ch)-1] = 'x'
# print(list.count('x'))
