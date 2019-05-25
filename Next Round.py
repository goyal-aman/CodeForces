#n, k = map(int, input().split())
#inpt = str(input())
#score_list = inpt.split()
#output = 0
#for i in range(n):
#    if (int(score_list[i]) >= int(score_list[k-1])) and int(score_list[i]) > 0:
#        output +=1
#    else:
 #       break
#print(output)


n, k = map(int, input().split())
score_list = list(map(int, input().split()))
output = 0
for i in range(n):
    if (score_list[i] >= score_list[k-1]) and score_list[i] > 0:
        output +=1
    else:
        break
print(output)







i=lambda:map(int,input().split())
n,k=i()
l=list(i())
print(      sum(    v >= max(1,l[k-1]) for v in l  )     )