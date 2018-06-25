import sys
import random
from collections import defaultdict

sys.setrecursionlimit(2024)

# creating random array
A = [random.randint(0, 10) for i in range(10)]
print(A)

MAX_CLOSED_TIME = 3
OPENED = set()
CACHE = defaultdict(int)


def get_cache_key(curr_hour, inside_air, time_left_to_be_closed):
    """
    The string formed from current hour, inside air value
    and time to left to be closed is the combination which uniquely specifies
    the current algorithm state.
    """
    return "%s_%s_%s" % (curr_hour, inside_air, time_left_to_be_closed)


def solve(curr_hour, inside_air, time_left_to_be_closed):

    # result is in cache return the result
    if get_cache_key(curr_hour, inside_air, time_left_to_be_closed) in CACHE:
        return CACHE[
            get_cache_key(curr_hour, inside_air, time_left_to_be_closed)]

    outside_air = A[curr_hour]

    # open open, there is no time to left
    if time_left_to_be_closed == 1:
        inside_air = outside_air
        return inside_air

    # we reached the end of the times in our calculations
    if curr_hour == len(A) - 1:
        return inside_air

    # assume we should open right now
    open_now = outside_air + solve(
        curr_hour + 1,
        outside_air,
        MAX_CLOSED_TIME)

    # assume we should stay closed
    stay_closed = inside_air + solve(
        curr_hour + 1,
        inside_air,
        time_left_to_be_closed - 1)

    # return the min value we get from our assumptions
    if open_now < stay_closed:
        OPENED.add(curr_hour)
        min_res = open_now
    else:
        if curr_hour in OPENED:
            OPENED.remove(curr_hour)
        min_res = stay_closed

    # cache the result
    CACHE[
        get_cache_key(curr_hour, inside_air, time_left_to_be_closed)] = min_res
    return min_res


print(solve(0, A[0], MAX_CLOSED_TIME))
print(OPENED)
