t = int(input())
for _ in range(t):
    total_money = int(input())

    spend = 0
    spent_total = 0
    while total_money>0:
        ml =  10** (len(str(total_money))-1)
        # print(f'total money: {total_money}, ml: {ml}')
        non_spent = total_money%ml
        # print(f"non spent; {non_spent}")
        spend = total_money - non_spent
        # print(f"spend : {spend}")
        total_money = total_money - spend + int(spend/10)
        spent_total += spend
    # print("output: ", end=' ')
    print(spent_total)
