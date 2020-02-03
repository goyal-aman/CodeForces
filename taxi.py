n = int(input())
li = [0,0,0,0,0]
for i in map(int, input().split()):
    li[i]+=1
#adding 4
total = li[4]
# print(f'debug total initial {total}')

#pairing 1 and 3
pair13 = min(li[1], li[3])
# print(f'this is pair13 {pair13}')
li[1]-=pair13
li[3]-=pair13
total += pair13
# print(f"this is total after pair13 {total}")
# print(f"this is li[1] and li[3] {li[1]} {li[3]} " )

#adding remaing 3
total += li[3]

#pairing 2
pair2 = li[2]//2
li[2]-= pair2*2
total += pair2
# print(f"debug: pair2 {pair2}")
# print(f"debug : total after pair 2: {pair2}")

#pair 1 and 2
if (li[2]):
    if li[1]<=2:
        total +=1
    else:
        li[1]-=2
        total+=1
        total += -((-li[1])//4)
else:
    total += -((-li[1])//4)
print(total)