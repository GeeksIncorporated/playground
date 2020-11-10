# https://leetcode.com/problems/brick-wall/description/
# There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
# The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
# If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.
# You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.
# 
# @lc app=leetcode id=554 lang=python
#
# [554] Brick Wall
#


from collections import defaultdict


# @lc code=start
class Solution:
    def leastBricks(self, wall):
        wall_length = len(wall)
        counter = defaultdict(int)
        for row in wall:
            c = 0
            for brick in row:
                c += brick
                counter[c] += 1
        first_max = second_max = 0
        for v in counter.values():
            if v > first_max:
                second_max = first_max
                first_max = v
            elif v > second_max:
                second_max = v
        return wall_length - second_max


# @lc code=end

s = Solution()
r = s.leastBricks([[1],[1],[1]])
print(r)