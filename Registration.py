a = {}
for i in range(int(input())):
    name = input()
    if not name in a:
        print('OK')
        a[name] = 0
    else:
        a[name] +=1
        print(name+ str(a[name]))