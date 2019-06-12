I = lambda:map(int, input().split())
strength, lvl = I()
for drgn_strn, bonus in sorted(list(I()) for _ in ' '*lvl):
    strength = (strength + bonus) * (strength > drgn_strn)
print('YNEOS'[strength==0::2])


# player_strength, lvl = map(int, input().split())
# data_input = []
# for _ in ' '*lvl:
#     data_input.append(list(map(int, input().split())))
#
# data_input.sort(key= lambda x: (x[0]))
#
# for i in data_input:
#     if player_strength > i[0]:
#         player_strength+=i[1]
#     else:
#         print('NO')
#         exit()
# else:
#     print("YES")
