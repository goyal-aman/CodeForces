s = input()
out = 0
for ch in s:
    if ch == '4' or ch == '7':
        out +=1
print(['NO','YES'][any(out == i for i in [4,7])])