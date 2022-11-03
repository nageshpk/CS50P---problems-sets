price = 50
while price > 0:
    print(f"Amount Due: {price}")
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5] and price > 0:
        price = price - coin
print(f"Change owed: {price * (-1)}")