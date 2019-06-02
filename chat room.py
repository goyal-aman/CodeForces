# s = input()
# i = -1
# d = ['h','e','l','l','o']
# for ch in d:
#     i = s.find(ch, i+1)
#     if i == -1:
#         print("NO")
#         exit()
# print("YES")

# alternate solution

s = iter(input())
print('NYOE S'[all(c in s for c in 'hello')::2])