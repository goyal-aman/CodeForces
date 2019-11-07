#solution 2
n = int(input())
li = []
index = 1
for i in map(int, input().split()):
    li += [index] * i
    index +=1
m = int(input())
for query in map(int, input().split()):
    print(li[query -1])




#solution 1
# def findRange(n, li, l, r):
#     mid = l + (r-l)//2
#     if abs(r -l) <= 1 :
#         return r
#     elif n> li[l] and n <= li[mid]:
#         return findRange(n, li,l, mid)
#     else:
#         return findRange(n, li, mid, r)
# n = int(input()) #number of piles
# a = [0] + ['' for _ in range(n)]
# index = 1
# s = 0
# for num in map(int, input().split()):
#     a[index]  = num + s
#     s = a[index]
#     index+=1

# m = int(input())
# li = list(map(int, input().split()))
# for num in li:
#     print(findRange(num, a, 0, len(a)-1))

