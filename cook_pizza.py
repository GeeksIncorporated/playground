import heapq as hq

from collections import defaultdict

h = []


def cook_pizza(orders_to_cooking_time):
    for k, v in list(orders_to_cooking_time.items()):
        if type(v) is not list:
            orders_to_cooking_time[k] = [v]

    def helper(ot):
        last_et = ot
        total_waiting_time = 0
        while len(h) > 0:
            pt, ot = hq.heappop(h)
            last_et += pt
            total_waiting_time += last_et - ot

            new_orders_times = [o for o in sorted_orders if o < last_et]

            for new_ot in new_orders_times:

                for pt in orders_to_cooking_time[new_ot]:
                    hq.heappush(h, (pt, new_ot))
                sorted_orders.remove(new_ot)
        return total_waiting_time / len(orders_to_cooking_time)

    wait_time = 0
    sorted_orders = sorted(orders_to_cooking_time.keys())

    while sorted_orders:
        ot = sorted_orders[0]
        for pt in orders_to_cooking_time[ot]:
            hq.heappush(h, (pt, ot))
        sorted_orders.remove(ot)
        wait_time += helper(ot)
    return wait_time

# orders = {
#     961148050: [385599125],
#     951133776: [376367013],
#     283280121: [782916802],
#     317664929: [898415172],
#     980913391: [847912645]}
#
# r = cook_pizza(orders)
# assert r == 1418670047, "Test: 1"
#
# orders = {0: [9], 10: [4]}
# r = cook_pizza(orders)
# print r
# assert r == 6, "Test: 2"

orders = defaultdict(list)
c = True
for line in open("cook_pizza_test_input"):
    if c:
        c = False
        continue
    ot, pt = list(map(int, line.strip().split(" ")))
    orders[ot].append(pt)

r = cook_pizza(orders)
print((r, 16673945929151))
# assert r == 16673945929151, "Test: 3"

