n = int(input())
s = list(map(int, input().split()))
max_s = max(s)
print(max_s*n - sum(s))