n = int(input())
# s = list(map(int, input().split()))
s = [[] for i in range(3)]
j = 0
for index, val in enumerate(map(int, input().split()), 1):
    (s[val-1]).append(index)
min_s = min(map(len, s))
print(min_s)
for i in zip(*s):
    print(*i)


# n = int(input())
# # s = list(map(int, input().split()))
# s = [[] for i in range(3)]
# j = 0
# for i in map(int, input().split()):
#     (s[i-1]).append(j)
#     j+=1
# min_s = len(min(s, key= lambda x: len(x)))
# print(min_s)
# if (min_s)>0:
#     for i in range(min_s):
#         print(s[0][i]+1,s[1][i]+1,s[2][i]+1)
