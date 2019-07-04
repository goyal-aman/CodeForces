import sys
n, m = map(int, input().split())
for i in range(n):
    t = sys.stdin.readline()
    if 'C' in t or 'M' in t or 'Y' in t:
        print('#Color')
        break
else:
    print('#Black&White')