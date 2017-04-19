import time
import sys
sys.setrecursionlimit(100000)
from collections import defaultdict

table = defaultdict(lambda: defaultdict(int))


def coins_change(n, coins):
    if table[n][len(coins)]:
        return table[n][len(coins)]

    if n == 0:
        return 1

    if n < 0 or len(coins) == 0:
        return 0

    table[n][len(coins)] = coins_change(n, coins[:-1]) + coins_change(n - coins[-1], coins)
    return table[n][len(coins)]


def coins_change_bottom_up(n, coins):
    table = defaultdict(lambda: defaultdict(int))
    for i in range(1, n + 1):
        table[i][1] = 1

    for j in range(2, len(coins) + 1):
        for i in range(1, n + 1):
            if i < coins[j - 1]:
                c = 0
            elif i == coins[j - 1]:
                c = 1
            else:
                c = table[i - coins[j - 1]][j]

            table[i][j] = table[i][j - 1] + c

    return table[i][j]

def coins_change_bottomup_short(n, coins):
    table = [1]+[0]*n
    for coin in coins: 
        for i in range(coin, n+1): 
            table[i] += table[i-coin] 
    return table[n]

n = 10000
coins = [1, 2, 3, 5]

st = time.time()
r = coins_change(n, coins)
t1 = time.time() - st
print r, t1

st = time.time()
r = coins_change_bottom_up(n, coins)
t2 = time.time() - st
print r, t2

print "Bottom up is faster x%.1f" % (float(t1)/t2)

