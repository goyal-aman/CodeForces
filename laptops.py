"""
by goyal-aman
https://codeforces.com/problemset/problem/456/A

note:
non efficient solution, question not clear.
"""

n = int(input())
pq = []
for _ in range(n):
    pq.append(list(map(int, input().split())))

pq.sort(key= lambda x : x[0]) #soritng based on price
# print(pq)
exist = 1
for i in range(n-1):
    if pq[i][1]>pq[i+1][1]:
        exist +=1
    if exist >1:
        print("Happy Alex")
        break
else:
    print("Poor Alex")