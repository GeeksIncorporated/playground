import inspect

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def nlogn(n, a, c):
    return np.multiply(np.multiply(a, n), np.log2(n)) + c


def quadratic(n, a, b, c):
    return n * a * np.power(n, 2) + np.multiply(n, b) + c


def cubic(n, a, b, c, d):
    return np.power(n, 3) * a + np.power(n, 2) * b + np.multiply(n, c) + d


def logn(n, a, c):
    return np.log2(n) * a + c


def line(n, a, b):
    return np.multiply(n, a) + b


def exponent(n, a, b):
    return np.multiply(a, np.power(2, n)) + b


import time


def scale(param_name, generator):
    def decorator(foo):
        def wrapper(*args, **kwargs):
            if not wrapper.initial:
                return foo(*args, **kwargs)
            wrapper.initial = False
            names = inspect.getargspec(foo)[0]
            ind = names.index(param_name)
            args = list(args)
            del args[ind]

            y = []

            for i, n in enumerate(generator):
                kwargs[param_name] = n
                st = time.time()
                foo(*args, **kwargs)
                end = time.time() - st
                print(end)
                y.append(end)

            y = np.array(y)
            y = y[abs(y - np.mean(y)) < np.std(y)]
            x = range(len(y))

            def fit(foo):
                popt, pcov = curve_fit(foo, x, y)
                res = foo(x, *popt)
                ss_res = np.sum(np.power((y - res), 2))
                ss_tot = np.sum(np.power(y - np.mean(y), 2))
                print(str(foo).split(" ")[1], "%.2f" % (1 - (ss_res / ss_tot)), popt, np.diag(pcov))
                plt.plot(res, '.')
                plt.show()

            plt.plot(x, y, '.')
            plt.show()

            fit(quadratic)
            fit(cubic)
            fit(line)
            # fit(logn)
            fit(exponent)

        wrapper.initial = True
        return wrapper

    return decorator


@scale("n", range(10, 25))
def test(n):
    res = []
    # if n < 0:
    #     return 1
    # return test(n-1) + test(n-2)

    for i in range(n**2):
        res.append(i)

@scale("n", range(10, 5000))
def testA(n):
    res = []
    # if n < 0:
    #     return 1
    # return test(n-1) + test(n-2)

    return sorted(range(n))

testA(1000)