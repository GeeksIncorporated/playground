import random


def roulette_wheel():
    a = random.randint(0, 36)
    if a in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34,
             36]:
        return "red"
    if a in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33,
             35]:
        return "black"
    if a in [0]:
        return "zero"


SERIES = 5


def gambling(stage, bet, money, pattern, result):
    while stage > 0:

        print(stage, bet, money, pattern, result)

        if result == "black":
            if pattern == SERIES:
                money += 2 * bet

            pattern = 0
            bet = 1

        elif result == "red":
            pattern += 1

            if pattern == SERIES:
                bet = min(200, bet * 2)
                money = money - bet

            if pattern == SERIES + 1:
                bet = 1
                pattern = 0

        elif result == "zero":
            pattern = 0
            bet = 1

        stage = stage - 1
        result = roulette_wheel()


print(gambling(1000000, 1, 100, 0, "zero"))
