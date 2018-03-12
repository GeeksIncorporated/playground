import sys
from collections import defaultdict

sys.setrecursionlimit(2024)


def mazgan(A, max_closed_in_a_row):

    cache = defaultdict(int)
    opened = defaultdict(int)

    print "In:", max_closed_in_a_row, A

    if max_closed_in_a_row == 1:
        return (sum(A), A)

    def solve(curr_hour, inside_air, time_left_to_be_closed):
        # we reached the end of the times in our calculations
        if curr_hour == len(A):
            return 0

        key = "%s_%s_%s" % (curr_hour,
                            inside_air,
                            time_left_to_be_closed)

        # result is in cache return the result
        if key in cache:
            return cache[key]

        outside_air = A[curr_hour]

        # open open, there is no time to left
        if time_left_to_be_closed == 1:
            return outside_air + solve(
                curr_hour + 1,
                outside_air,
                max_closed_in_a_row)

        # assume we should open right now
        open_now = outside_air + solve(
            curr_hour + 1,
            outside_air,
            max_closed_in_a_row)

        # assume we should stay closed
        stay_closed = inside_air + solve(
            curr_hour + 1,
            inside_air,
            time_left_to_be_closed - 1)

        # return the min value we get from our assumptions
        if open_now <= stay_closed:
            opened[curr_hour] += 1
            min_res = open_now
        else:
            opened[curr_hour] -= 1
            min_res = stay_closed

        # cache the result
        cache[key] = min_res
        return min_res

    integral = (solve(0, A[0], max_closed_in_a_row))

    # filter the indeces dict by positive values (those hours when was opened
    # more times than closed)
    indices_when_opened_more_times_than_closed = [
        k for k, v in opened.items() if v > 0]
    return integral, indices_when_opened_more_times_than_closed


A = [1, 2, 3, 4, 5]
assert mazgan(A, 10) == (5, [0])

A = [1, 5, 5, 5]
assert mazgan(A, 3) == (8, [0, 3])

A = [1, 5, 0, 5]
assert mazgan(A, 3) == (2, [0, 2])

A = [1, 2, 3, 4, 5, 0, 1]
assert mazgan(A, 3) == (11, [0, 2, 5])

A = [1, 5, 1, 5]
assert mazgan(A, 1) == (12, [1, 5, 1, 5])

A = [3, 2, 1, 0, 9, 8, 7]
assert mazgan(A, 3) == (13, [0, 1, 2, 3, 6])

# creating random array
import random
A = [random.randint(0, 10) for i in range(20)]

time_left_till_forced_opened = random.randint(1, len(A) / 2)
print(mazgan(A, time_left_till_forced_opened))
