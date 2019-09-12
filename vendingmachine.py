from framework import *

usd_coins = [100, 50, 25, 10, 5, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]
usd_coins_left = [0, 1, 2, 1, 2, 5]
eur_coins_left = [1, 0, 2, 0, 0, 3, 4]

def get_change(amount, coins=eur_coins, coins_left=eur_coins_left):
    change = []
    coin_amount = 0
    for coin in coins:
        while coins_left[2] > 0:
            while coin <= amount:
                amount -= coin
                change.append(coin)
                coin_amount += 1
            
    return change

test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2,1])
test_are_equal(get_change(7), [5,2])
test_are_equal(get_change(9), [5,2,2])
test_are_equal(get_change(35, usd_coins), [25,10])
test_are_equal(get_change(50), [20, 20, 2, 2, 2, 1, 1, 1, 2])