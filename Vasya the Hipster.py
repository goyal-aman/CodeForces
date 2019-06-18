red, blue = map(int, input().split())
big, small = max(red, blue), min(red, blue)
print(small, (big-small)//2)