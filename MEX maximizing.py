q,x = map(int, input().split())
li = [0]*x
output = []
mx = 0
for _ in range(q):
    jth = int(input())
    li[jth%x]+=1
    while li[mx%x]:
        li[mx%x]-=1
        mx+=1
    output.append(mx)
print(*output)
# print(" ".join(output))
    # print(mx)
    # min_cnt = min(li)
    # indx = li.index(min_cnt)
    # print(x*min_cnt + indx )
# print(li)