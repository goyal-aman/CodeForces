'''
by goyal-aman
https://codeforces.com/problemset/status
'''

li = list(map(int, input().split()))
cal = sum([li[int(ch)-1] for ch in input() ])
print(cal)