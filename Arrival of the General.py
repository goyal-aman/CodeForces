n = int(input())
s = list(map(int, input().split()))
a, b = s.index(max(s)), s[::-1].index(min(s))
print(a+b - ((a+b)>=n))
#
# count1, count2 = 0,0
# print(s)
# while s[0] != a:
#     c = s.index(a)
#     while c > 0:
#         s[c-1], s[c] = s[c], s[c-1]
#         c-=1
#         count1 +=1
# print(s)
# while s[n-1] != b:
#     t= s[::-1].index(b)
#     d = n - t -1
#     while d < n-1: #n:4
#         s[d+1], s[d] = s[d], s[d+1]
#         d+=1
#         count2+=1
# print(s)
# print(count1+count2)