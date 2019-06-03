s = input()
if len(s) >1:
    if s.isupper():
        print(s.lower())
    elif s[0].islower() and s[1:].isupper():
        print(f'{s[0].upper()}{s[1:].lower()}')
    else:
        print(s)
else:
    if s.isupper():
        print(s.lower())
    elif s.islower():
        print(s.upper())
