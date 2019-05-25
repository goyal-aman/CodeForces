str1 = input().lower()
str2 = input().lower()
#for i in range(len(str1)):
#    if str1 == str2:
#        print('0')
#        break
#    elif str1[i] != str2[i]:
#        print( '1' if ord(str1[i]) > ord(str2[i]) else '-1')
#
#        break
str1 = input().lower()
str2 = input().lower()
print( (str1>str2) - (str1<str2) )