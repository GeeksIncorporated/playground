import unittest


class MyTestCase(unittest.TestCase):
    def ransom_note(self,magazine, ransom):
        magazine = sorted(magazine.split(' '))
        ransom = sorted(ransom.split(' '))

        while magazine and ransom:

            if ransom[0] < magazine[0]:
                return False
            elif ransom[0] == magazine[0]:
                ransom.pop(0)
                magazine.pop(0)
            else:
                magazine.pop(0)
        if ransom:
            return False
        return True

    def test_something(self):
        self.ransom_note(
            "give me one grand today night",
            "give one grand today today"
        )


if __name__ == '__main__':
    unittest.main()
