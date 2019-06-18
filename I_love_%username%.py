n = int(input())
s = list(map(int, input().split()))
amazing = 0
for i in range(n):
    if i > 0 and not s[i] in s[:i]:
        if s[i] < min(s[:i]) or s[i] > max(s[:i]):
            amazing +=1
print(amazing)