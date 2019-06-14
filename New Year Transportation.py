n, t = map(int, input().split())
s = list(map(int , input().split()))
tile = 1
for i in s:
    while tile<=t:
        tile += s[tile-1]
        if tile == t:
            print('YES')
            exit()
    else:
        print('NO')
        exit()