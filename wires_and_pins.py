from collections import defaultdict

LEFT = 0
RIGHT = 1

wires = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["A", "C"]
}

pins = defaultdict(lambda: {"side": None})
pins_pool = wires.keys()


def split_wires():

    if len(pins_pool) == 0:
        print pins
        return

    pin = pins_pool.pop()

    for side in (LEFT, RIGHT):
        if is_safe(pin, side):
            pins[pin]["side"] = side
            split_wires()

def is_safe(pin, side):
    for child in wires[pin]:
        if pins[child]["side"] == side:
            return False
    return True

split_wires()