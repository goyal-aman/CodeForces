bog = input().lower()
temp = ''
for i in bog:
    if not i in temp:
        temp += i

print(['CHAT WITH HER!','IGNORE HIM!'][len(temp)%2!=0])
