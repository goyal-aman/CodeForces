import sys
def thanos(li, len_li):
    if li[:] == sorted(li):
        return len_li
    return max(thanos(li[:len_li // 2], len_li // 2), thanos(li[len_li // 2:], len_li // 2))

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
print(thanos(s,n))