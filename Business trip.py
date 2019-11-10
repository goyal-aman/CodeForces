"""
by goyal-aman
https://codeforces.com/problemset/problem/149/A
"""

k = int(input())
li = sorted(list(map(int, input().split())), reverse=True)
num_months = 0
height = 0
index = 0
while  height <k and index<12:
    height += li[index]
    index +=1
    num_months +=1

print(num_months if height>=k else -1)