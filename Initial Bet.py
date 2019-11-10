"""
by goyal-aman
https://codeforces.com/problemset/problem/478/A
"""

li = list(map(int, input().split()))
sum_li = sum(li)
if sum_li%5==0 and sum_li:
    print(sum_li//5)
else:
    print('-1')