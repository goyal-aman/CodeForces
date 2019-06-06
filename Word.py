s =input()
print([s.upper(),s.lower()][sum(ch >= '[' for ch in s)>= len(s)/2])
