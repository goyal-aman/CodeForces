player_strength, lvl = map(int, input().split())
data_input = []
for _ in ' '*lvl:
    data_input.append(list(map(int, input().split())))

data_input.sort(key= lambda x: (x[0]))

for i in data_input:
    if player_strength > i[0]:
        player_strength+=i[1]
    else:
        print('NO')
        exit()
else:
    print("YES")
