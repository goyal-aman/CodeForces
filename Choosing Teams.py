n,k = map(int, input().split())
s = list(map(int, input().split()))
print(sum(i<=5-k for i in s)//3)

# n,k = map(int, input().split())
# s = list(map(int, input().split()))
# i: int
# t = [i for i in s if i <=5-k]
# print(int(len(t)/3))