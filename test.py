a,b = map(int, input("Enter two values").split())
c = [a,b][a>b] #this is like a ternary operator in c
               # return b on TRUE, a on FALSE
print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')