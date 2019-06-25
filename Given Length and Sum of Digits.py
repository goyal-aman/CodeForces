#NOT SELF COMPLETEDk
m,s = map(int,input().split())


if s> 9*m or (s<1 and m>1):
    print(-1, -1)
    exit()
#for min
index = m-1
min_s = s
while index >=0:
    pos = max(0, min_s - 9*index)
    if index == m-1 and min_s>0 and pos==0:
        pos = 1
    print(pos, end='')
    index-=1
    min_s-=pos

print(' ', end='')

#for max
index = m - 1
max_s = s
while index>=0:
    val = min(9, max_s)
    print(val, end='')
    max_s-=val
    index-=1
