s = input()
p = input()
for i in range(len(s)):
    if s[i] != p[i]:
        print('1',end='')
    else:
        print('0',end='')