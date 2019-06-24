n = int(input())
s = list(map(int, input().split()))
max_s = max(s)
print(sum(max_s-i for i in s))