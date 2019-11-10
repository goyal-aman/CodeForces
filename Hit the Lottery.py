"""
by goyal-aman
https://codeforces.com/problemset/problem/996/A
"""

n = int(input())
currency = [1 , 5, 10, 20, 100]
notes = 0
for val in currency[::-1]:
    notes += n//val
    n = n%val
print(notes)
