user_input = int(input())
output =0
for i in range(user_input):
    view = list(map(int, input().split()))
    total = 0
    for n in view:
        total += n
        if total>=2:
            output +=1#
print(output)



#print(sum(input("one: ").count('1')   >   1 for x in [0]*int( input("two: "))))
