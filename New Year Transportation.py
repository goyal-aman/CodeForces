n, t = map(int, input().split())
s = list(map(int , input().split()))
tile = 1
try:
    for i in s:
        tile += s[tile - 1]
        if tile == t:
            print('YES')
            exit()
    else:
        print('NO')
except IndexError:
    print('NO')