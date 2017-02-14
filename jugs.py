j = {
    "A": [230, 240],
    "B": [290, 310],
    "C": [500, 515]
}

required_constraint = [2100, 2300]
solution = []


def solve(jugs, remaining_constraints):
    if remaining_constraints[0] > required_constraint[0] and \
                    remaining_constraints[1] < required_constraint[1]:
        print solution
    elif remaining_constraints[1] > required_constraint[1]:
        return False

    for j, cj in jugs.items():
        # make a guess
        solution.append(j)
        remaining_constraints[0] += cj[0]
        remaining_constraints[1] += cj[1]
        solve(jugs, remaining_constraints)

        # backtrack last guess
        solution.pop()
        remaining_constraints[0] -= cj[0]
        remaining_constraints[1] -= cj[1]

if __name__ == "__main__":
    solve(j, [0, 0])
