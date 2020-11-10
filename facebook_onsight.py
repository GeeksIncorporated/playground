# write a parser fo arithmetic expression for example:
# 1 + 5 * ( 1 - 2 )
# will return -4


def solve(E):
    """
    Problem of priority on multiplication and division operations
    D(0,n) = D(0,i)  D(i+1,n)
    each of which:
    splits to the following problems ( on i-th place adn ) on j-th place
    D(0,n) = D(0,i) + D(i+1,j) + D(j+1,n)

    1 + 2 * 3 + 4*(5+6)

    :param E:
    :return:
    """
    operations = {"+", "-", "*", "/"}
    digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    stack = []
    number = 0
    for c in E:
        if c in digits:
            number = 10*number + int(c)
            continue

        if c == "+":
            stack.append(number)
        elif c == "-":
            stack.append(number)
        elif c == "*":
            pass