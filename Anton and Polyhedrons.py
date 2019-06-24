from collections import Counter
source = {'Tetrahedron': 4,
     'Cube': 6,
     'Octahedron': 8,
     'Dodecahedron': 12,
     'Icosahedron':20
          }
face = 0
s = []
for _ in range(int(input())):
    s.append(input())
s = dict(Counter(s))
for i in s:
    face+= s[i] * source[i]
print(face)
# _________________________


# l = {'Tetrahedron': 4,
#      'Cube': 6,
#      'Octahedron': 8,
#      'Dodecahedron': 12,
#      'Icosahedron':20
#      }
# face = 0
# for _ in range(int(input())):
#     s = input()
#     face += l[s]
# print(face)