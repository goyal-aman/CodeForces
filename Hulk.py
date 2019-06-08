n = int(input())
l = ['I love', 'I hate']
a = l*n
print(' that '.join(a[:n])+ ' it')
# l = [' I love', ' I hate']
# n = int(input())
# str = ''
# for i in range(1,n+1):
#     str += l[i%2] + ' that'
# print(str[:len(str)-5] + ' it')
