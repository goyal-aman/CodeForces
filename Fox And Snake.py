n, m = map(int, input().split())
for i in range(n):
    # print(i%4)
    print(['#'*m,'.'*(m-1)+'#',m*'#', '#'+'.'*(m-1)][i%4])


# n,m = map(int,(input().split()))
# line = 1
# body, curve = 1, 1
# while line<= n:
#     if body&1 and line <=n:
#         print('#'*m,)
#         line +=1
#     if (curve&1)and line <=n:
#         print('.'*(m-1),end="")
#         print('#')
#         line+=1
#         curve+=1
#     elif not(curve&1) and line <=n:
#         print('#',end="")
#         print('.'*(m-1))
#         line+=1
#         curve+=1
