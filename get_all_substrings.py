from collections import defaultdict

subs = set()


def get_all_substrings_top_down(s, i, j):
    if i > j or i < 0:
        return 0

    if (i, j) in subs:
        return 0

    subs.add((i, j))

    if i == 0 and j == 0:
        return 1

    get_all_substrings_top_down(s, i - 1, j - 1),
    get_all_substrings_top_down(s, i, j - 1),
    get_all_substrings_top_down(s, i - 1, j)


def get_all_substrings_bottom_up(s):
    n = len(s)
    T = defaultdict(lambda : defaultdict(int))
    for p in range(n):
        T[p][p] = p

    for i in range(n):
        for j in range(i+1, n):
            T[i][j] = T[i][j-1]
    return T


s = "012"
# get_all_substrings_top_down(s, len(s) - 1, len(s) - 1)
# for sub in sorted(subs):
#     print s[sub[0]: sub[1] + 1]

T = get_all_substrings_bottom_up(s)
print T[0][2]
