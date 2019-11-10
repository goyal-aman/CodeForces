'''
https://codeforces.com/problemset/problem/706/B
by goyal-aman 
'''
def findIndex(num, li, lo, hi):
    while lo<hi:
        mid = (lo + hi)>>1
        if num < li[mid]: hi = mid
        else : lo = mid + 1
    return lo


n = int(input())
prices = sorted(map(int, input().split()))
# print(prices)
q = int(input())
for _ in range(q):
    money = int(input())
    options = findIndex(money, prices, 0, len(prices))
    print(options)
