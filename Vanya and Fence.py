n, h = map(int, input().split())
s = list(map(int, input().split()))
print(sum((i > h)+1 for i in s))
#
# c = 0
# for i in s:
#     c += 2 if i>h else 1
# print(c)