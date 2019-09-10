n = int(input())
t = n
p = 2
while p<=t:
    z = p*(t-p) + 1
    n += z
    p+=1
print(n)
