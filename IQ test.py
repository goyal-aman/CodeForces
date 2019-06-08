input()
s = list(map(lambda x: int(x) % 2, input().split()))
print(s.index(sum(s) == 1)+1)

# n = int(input())
# lst = list(map(int, input().split()))
# odd, even = 0, 0
#
# for i in range(3):
#     if lst[i]%2:
#         odd+=1
# if odd>1:
#     odd = 0
# else:
#     odd = 1
# for ch in lst:
#     if ch%2==odd:
#         print(lst.index(ch)+1)
#         break