"""
by goyal-aman
https://codeforces.com/problemset/problem/467/B
"""

def isFriend(all_armies, fedors_army, k):
    num_friends = 0
    for army in all_armies:
        match = army ^ fedors_army
        num_friends += 1 if (bin(match).count('1') <= k) else 0 
    return num_friends
        
    
    
    return bin(match).count('1') <= k

if __name__ == "__main__":
    num_friends = 0
    all_armies = []

    n,m,k = map(int, input().split())
    for _ in range(m):
        all_armies.append(int(input()))
    fedors_army = int(input())
    print(isFriend(all_armies, fedors_army, k))