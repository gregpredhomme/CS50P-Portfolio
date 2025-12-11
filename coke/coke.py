
def check_currency(c):
    if c == 25 or c == 10 or c == 5:
        return True

cost = 50
while True:
    print(f"Amount Due: {cost}")
    coin = int(input('Insert Coin: '))
    if check_currency(coin) is True:
        cost -= coin
    if cost <= 0:
        cost = abs(cost)
        print(f"Change Owed: {cost}")
        break







