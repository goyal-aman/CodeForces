import bisect

def findIndex(num, li, lo, hi):
    while lo<hi:
        mid = (lo + hi)>>1
        if num < li[mid]: hi = mid
        else : lo = mid + 1
    return lo

# li = [1,2,3,5,6,7,8,9]
# num = 10
# print(findIndex(num,li, 0, len(li)-1))

n = int(input())
prices = sorted(map(int, input().split()))
# print(prices)
q = int(input())
for _ in range(q):
    money = int(input())
    options = findIndex(money, prices, 0, len(prices))
    print(options)
    print(f'from bisect : {bisect.bisect(prices, money)}')
