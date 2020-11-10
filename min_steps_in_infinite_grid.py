class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer

    def go_to_point(self, from_point, to_point):
        steps = 0
        steps = max(abs(from_point[0] - to_point[0]), abs(from_point[1] - to_point[1]))
        return steps

    def coverPoints(self, X, Y):
        points = list(zip(X, Y))
        start = list(points[0])
        steps = 0
        for point in points[1:]:
            steps += self.go_to_point(list(start), list(point))
            start = point
        return steps

s = Solution()
print(s.coverPoints([0, 3], [0, 5]))