import sys

sys.setrecursionlimit(2000)


cache = {}


def solve(balls, floors):
    if balls < 2 or len(floors) < 2:
        return len(floors)

    if (balls, len(floors)) in cache:
        return cache[(balls, len(floors))]

    min_res = sys.maxsize
    for i in range(len(floors)):
        res = max(solve(balls, floors[i + 1:]), solve(balls - 1, floors[:i]))
        if min_res > res:
            min_res = res
    cache[(balls, len(floors))] = min_res + 1
    return min_res + 1


balls = 2
floors = 100
print((solve(balls, list(range(1, floors)))))

# Empirical complexity estimates like Nlogk
# Times are as following:
# floors            balls      tries    seconds
# Floors: 100 Balls: 2 14 0.0242478847504
# Floors: 200 Balls: 2 20 0.0411851406097
# Floors: 300 Balls: 2 24 0.077220916748
# Floors: 400 Balls: 2 28 0.143841028214
# Floors: 500 Balls: 2 32 0.247375965118
# Floors: 600 Balls: 2 35 0.399200201035
# Floors: 700 Balls: 2 37 0.596392154694
# Floors: 800 Balls: 2 40 0.852401018143
# Floors: 900 Balls: 2 42 1.19441890717
# Floors: 1000 Balls:  1 1000 4.79221343994e-05
# Floors: 1000 Balls:  2 45 0.406578063965
# Floors: 1000 Balls:  3 19 1.82901287079
# Floors: 1000 Balls:  4 13 1.84065389633
# Floors: 1000 Balls:  5 11 1.82535195351
# Floors: 1000 Balls:  6 11 1.82970023155
# Floors: 1000 Balls:  7 11 1.95147514343
# Floors: 1000 Balls:  8 10 1.89832186699
# Floors: 1000 Balls:  9 10 1.84272408485
