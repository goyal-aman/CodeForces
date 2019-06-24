#NOT SELF SOLVED

l = ['Sheldon','Leonard','Penny','Rajesh','Howard']
n = int(input()) # taking input from user to print the name of the person
                 # standing at that position

i = 0
while n>(len(l)*2**i):
    n = n - len(l)* (2**i)
    i = i + 1

index = int((n-1)/(2**i ))

print(l[index])