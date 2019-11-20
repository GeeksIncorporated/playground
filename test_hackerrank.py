
import re
import unittest

END_PATTERN = re.compile("__end__")

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.contacts_root = dict()

    def count_words(self, t):
        ends = 0
        for c in t:
            if c != "__end__":
                ends += self.count_words(t[c])
            elif c == "__end__":
                ends += 1
        # self.cached_counts[key] = ends
        return ends

    def test_something(self):
        res = []
        with open("/home/aliowka/Documents/sample_input_100000") as input:
            input = input.read().split("\n")
            self.process(input, res)

        with open("/home/aliowka/Documents/sample_output_100000") as f:
            expected = f.read().split("\n")
        self.validate_result(expected, res)

    def test_something1(self):
        res = []
        input = """add hack
add hackerrank
find hac
find hak""".split("\n")
        self.process(input, res)
        expected = ["2","0"]
        self.validate_result(expected, res)

    def process(self, input, res):
        n = 0
        for line in input:
            op, contact = line.strip().split(' ')

            if op == "add":
                current_dict = self.contacts_root
                for char in contact:
                    if char not in current_dict:
                        current_dict[char] = {"common_words": 0}
                    current_dict = current_dict[char]
                    current_dict["common_words"] += 1
                current_dict["__end__"] = "$"

            if n % 1000 == 0:
                print n
            n += 1

            if op == "find":
                current_dict = self.contacts_root
                for char in contact:
                    current_dict = current_dict.get(char, {})
                    if not current_dict:
                        break
                common_words = current_dict.get("common_words", 0)
                res.append(common_words)

    def validate_result(self, expected, res):
        l = min(len(res), len(expected))
        for i in xrange(l):
            self.assertEqual(str(res[i]), expected[i])
        print "Done"


if __name__ == '__main__':
    unittest.main()
