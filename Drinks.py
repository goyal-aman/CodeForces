n = int(input())
s = list(map(int, input().split()))
print(float(sum((1/n*i) for i in s)))
