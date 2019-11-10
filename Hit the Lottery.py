"""
by goyal-aman
https://codeforces.com/problemset/problem/996/A
"""

def notes(money):
  currency = [1 , 5, 10, 20, 100]
  notes = 0
  for val in currency[::-1]:
    notes += n//val
    n = n%val
  print(notes)


#solution 2
n = int(input)
def notes2(money):
  print( (money//100) + (money%100)//20 + (money%20)//10 + (money%10)//5 + money%5)

