a = set(input())
str = ''
for ch in a:
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
        str += ch
print(len(str))