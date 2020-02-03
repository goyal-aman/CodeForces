t = int(input())
for _ in range(t):
    n = int(input())
    li = [(0,0)]
    for _ in range(n):
        x,y = map(int, input().split())
        li.append( (x,y) )
    li.sort(key=lambda x: (x[0], x[1]))

    prev_x , prev_y = li[0][0], li[0][1]
    step = []
    for cord in li:
        x, y = cord[0], cord[1]
        nx, ny = x-prev_x, y-prev_y
        if y<prev_y:
            print("NO")
            break
        t = 'R'*nx + 'U'*ny
        step.append(t)
        prev_x, prev_y = cord[0], cord[1]
    else:
        print('YES')
    
    # print(li)
        a = ''.join(step)
        print(a)
        


# li = [(1,20), (1,3), (1,4), (2,6), (2,8)]
# li.sort(key=lambda x: (x[0], -x[1]))
# print(li)