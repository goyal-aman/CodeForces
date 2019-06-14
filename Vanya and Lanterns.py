n,l = map(int, input().split())
coords = [0]
coords.append(sorted(list(map(int, input().split()))))
# print(coords)
# print(list(zip(coords, coords[1:])))
# print(l, max(y-x for x,y in zip(coords, coords[1:])))
a = max(y-x for x,y in zip(coords, coords[1:]))/2
b = min(y-x for x,y in zip(coords, coords[1:]))
print([b,a][b>a])
