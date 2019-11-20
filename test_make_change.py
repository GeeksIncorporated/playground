
import unittest



class MyTestCase(unittest.TestCase):
    change = []
    good_results = set()
    cache = {}

    def make_change(self, coins, n):

        total = sum (self.change)

        if total == n:
            print self.change
            self.good_results.add(str(sorted(self.change)))
            self.change.pop(0)
            return 1

        elif total > n:
            self.change.pop(0)
            return 0

        elif total < n:
            s = 0

            while coins:
                c = coins.pop(0)
                self.change.append(c)
                s += self.make_change(coins, n)

            if self.change:
                self.change.pop(0)

            return s

    def test_make_change(self):
        n = 6
        coins = [1,2]
        coins_large = []
        for c in coins:
            coins_large.extend([c] * (n / c))
        self.make_change(coins_large, n)
        print len(self.good_results), self.good_results
        print self.cache


if __name__ == '__main__':
    unittest.main()
