
#LIST OF SQUARE OF PRIMES
l = 10**6
bool_list = [1]*l
square_of_primes = {0}
for p in range(2,l):
    if bool_list[p]:
        for j in range(p*p, l, p):
            bool_list[j] = 0
        #p is prime, p*p is T-prime
        square_of_primes.add(p*p)

#MAIN
input()
for d in map(int, input().split()):
    if d in square_of_primes:
        print('YES')
    else:
        print('NO')