# Problem 21.1 page 163

doors = [False] * 500

def check_perfect_square(n):
    sqrt = int(pow(n, 0.5))
    return pow(sqrt, 2) == n

def solve(doors):
    counter = 0
    for i in range(1, len(doors)):
        if check_perfect_square(i):
            counter += 1
    return counter

print((solve(doors)))