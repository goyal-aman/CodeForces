n = input()
print(n if int(n)>-1 else max(int(n[:-1]), int(n[:-2] + n[-1])))