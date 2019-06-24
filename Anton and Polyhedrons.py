source = {'Tetrahedron': 4,
     'Cube': 6,
     'Octahedron': 8,
     'Dodecahedron': 12,
     'Icosahedron':20
          }


n = int(input())
print(sum(source[input()] for _ in range(n)))

# source = {'Tetrahedron': 4,
#      'Cube': 6,
#      'Octahedron': 8,
#      'Dodecahedron': 12,
#      'Icosahedron':20
#           }
# target = {'Tetrahedron': 0,
#      'Cube': 0,
#      'Octahedron': 0,
#      'Dodecahedron': 0,
#      'Icosahedron':0
#           }
#
# l = [0]*5
# for _ in range(int(input())):
#     target[input()] += 1
#
# # print(target)
#
# face = 0
# for i in target:
#     face += target[i]*source[i]
# print(face)

# ______________________________
# from collections import Counter
# source = {'Tetrahedron': 4,
#      'Cube': 6,
#      'Octahedron': 8,
#      'Dodecahedron': 12,
#      'Icosahedron':20
#           }
# face = 0
# s = []
# for _ in range(int(input())):
#     s.append(input())
# s = dict(Counter(s))
# for i in s:
#     face+= s[i] * source[i]
# print(face)
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