import unittest

class MyTestCase(unittest.TestCase):

    def sorted_numeraed_set(self, a, b):
        n = 0
        a = sorted(a)
        b = sorted(b)

        while True:
            if not a:
                n += len(b)
                return n
            if not b:
                n += len(a)
                return n

            if a[0] == b[0]:
                a.pop(0)
                b.pop(0)
            elif a[0] < b[0]:
                a.pop(0)
                n += 1
            elif a[0] > b[0]:
                b.pop(0)
                n += 1


    def test_something(self):
        self.assertEqual(self.sorted_numeraed_set("abc", "cde"), 4)


if __name__ == '__main__':
    unittest.main()
