j = {
    "A": [230, 240],
    "B": [290, 310],
    "C": [500, 515]
}

required_constraint = [2100, 2300]
solution = []


def solve(jugs, constraints):
    if constraints[0] > required_constraint[0] and \
                    constraints[1] < required_constraint[1]:
        print solution

    elif constraints[1] > required_constraint[1]:
        return False

    for j, cj in jugs.items():
        # make a guess
        solution.append(j)
        solve(jugs, (constraints[0] +cj[0], constraints[1] +cj[1]))
        #backtrack last gues
        solution.pop()


if __name__ == "__main__":
    solve(j, [0, 0])
