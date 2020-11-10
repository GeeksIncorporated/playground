class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        digits = []
        while A:
            digits.insert(0, A % 10)
            A /= 10

        s = set()
        for i in range(len(digits)):
            product = 1
            for j in range(i, len(digits)):
                product *= digits[j]
                if product in s:
                    return False
                s.add(product)
        return True

s = Solution()
print(s.colorful(2345))
