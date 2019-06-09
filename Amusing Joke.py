str1 = input()
str2 =  sorted(input() + str1)
str3 = sorted(input())
print(['NO','YES'][str2==str3])