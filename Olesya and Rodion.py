n, t = input().split()
if int(n)<len(t):
    print(-1)
else:
    print(f"{t}", end='')
    print('0' * (int(n) - len(t)))

'''
n:4
t:9
9 000

n:4
t:11
1100
'''
