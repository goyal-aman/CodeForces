n,t = map(int , input().split())
s = list(map(int, input().split()))
i = 1
while i < t:
    i+=s[i-1]
print('YNEOS'[i>t ::2])


# n, t = map(int, input().split())
# s = list(map(int , input().split()))
# tile = 1
# try:
#     for i in s:
#         tile += s[tile - 1]
#         if tile == t:
#             print('YES')
#             exit()
#     else:
#         print('NO')
# except IndexError:
#     print('NO')
#


# n, t = map(int, input().split())
# s = list(map(int , input().split()))
# tile = 1
# for i in s:
#     while tile<=t:
#         tile += s[tile-1]
#         if tile == t:
#             print('YES')
#             exit()
#     else:
#         print('NO')
#         exit()