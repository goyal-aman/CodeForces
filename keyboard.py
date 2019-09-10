li = 'qwertyuiopasdfghjkl;zxcvbnm,./'
c = []
ch = [-1, 1][input() == 'L']
line = input()
for i in line:
    c.append(li[li.index(i)+ch])
print(''.join(c))