n = int(input())
boys = sorted(map(int, input().split()))

m = int(input())
girls = sorted(map(int, input().split()))
# print(boys, girls)
i,j,k = 0,0,0
while i<n and j<m:
    if abs(boys[i]-girls[j])<=1:
        i+=1
        j+=1
        k+=1
    elif boys[i]<girls[j]:
        i+=1
    else:
        j+=1
print(k)