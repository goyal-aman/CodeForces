"""
by goyal.aman
https://codeforces.com/problemset/problem/599/A

note:
patrick can visit first any shop

a : home -> shop1
b : home -> shop2
c : shop1 - shop2

possible routes:
          home
        /       \
     shop1 ---- shop2

home - shop1 - shop2 - home

home - shop1 - shop2 - shop1 - home
home - shop2 - shop1 - shop2 - home

home - shop1 - home - shop2 - home <2 ways>
"""
a,b,c = map(int, input().split())
route1 = a + c + b
route2 = a + c + c + a
route3 = b  + c + c + b
route4 = a + a + b + b
print(min(route1, route2, route3, route4))
