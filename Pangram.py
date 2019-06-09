input()
s = set(input().lower())
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in l:
    if not i in s:
        print('NO')
        break
else:
    print('YES')