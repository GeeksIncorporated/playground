import random

# a = [random.randint(1, 10) for i in range(10)]

a = [10, 2, 6, 9, 3, 6, 2, 6, 9, 6]
def switch(i, j):
    a[i], a[j] = a[j], a[i]


def sort_dutch_flag(m):
    l = 0
    r = len(a) - 1
    ml = mr = m

    while l < ml or mr < r:

        if a[l] == a[ml]:
            switch(l, ml - 1)
            ml -= 1

        elif a[l] > a[ml]:
            switch(l, r)
            r = max(mr, r-1)

        else:
            l = min(l+1, ml)

        if a[mr] == a[r]:
            switch(mr + 1, r)
            mr += 1

        elif a[r] < a[mr]:
            switch(l, r)
            l = max(l+1, ml)

        else:
            r = max(mr, r - 1)


i = 4
print a, a[i]
sort_dutch_flag(i)
print a
