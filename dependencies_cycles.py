# https://www.interviewbit.com/problems/possibility-of-finishing-all-courses-given-pre-requisites/

# Possibility of finishing all courses given pre-requisites
# Problem Setter: mihai.gheorghe
# Problem Tester: sneh_gupta
#
#     There are a total of N courses you have to take, labeled from 1 to N. Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses. return 1/0 if it is possible/not possible.
# The list of prerequisite pair are given in two integer arrays B and C where B[i] is a prerequisite for C[i].
#
#     Example:
#
#     If N = 3 and the prerequisite pairs are [1,2] and [2,3], then you can finish courses in the following order: 1, 2 and 3.
#     But if N = 2 and the prerequisite pairs are [1,2] and [2,1], then it is not possible for you to finish all the courses.
#
# This is a classic algorithm for identifying dependencies cycles!
#


from collections import defaultdict


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        G = defaultdict(set)
        for i, p in enumerate(B):
            G[C[i]].add(p)

        unresolved = set()
        resolved = set()

        def solve(node):
            unresolved.add(node)
            for dependency in G[node]:
                if dependency in resolved:
                    continue
                if dependency in unresolved:
                    return False
                if not solve(dependency):
                    return False

            resolved.add(node)
            unresolved.remove(node)
            return True

        for b in B:
            if b in resolved:
                continue
            solve(b)
        return int(len(unresolved) == 0)


s = Solution()

A = 66
B = [36, 53, 1, 12, 16, 2, 21, 8, 57, 37, 19, 33, 33, 19, 30, 18, 6, 63, 46, 23, 42, 13, 22, 32, 9, 9, 36, 46, 63, 66,
     28, 58, 31, 43, 44, 15, 45, 54, 50, 64, 16, 51, 54, 17, 60, 8, 22, 6, 32, 12, 7, 40, 50, 13, 29, 3, 42, 58, 20, 52,
     26, 28, 49, 13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
     29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
C = [17, 64, 30, 48, 41, 57, 56, 65, 47, 23, 15, 66, 37, 41, 59, 45, 4, 4, 34, 2, 62, 51, 24, 20, 3, 11, 43, 39, 56, 34,
     9, 47, 65, 14, 35, 10, 27, 31, 5, 24, 38, 5, 53, 10, 38, 55, 35, 39, 26, 38, 14, 52, 27, 25, 55, 40, 28, 59, 18, 7,
     21, 29, 8, 48, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1]
assert s.solve(A, B, C) == 0

A = 3
B = [1, 2, 3, 5]
C = [2, 3, 4, 6]
assert s.solve(A, B, C) == 1

A = 3
B = [1, 2, 3]
C = [2, 3, 2]
assert s.solve(A, B, C) == 0

A = 5
B = [1, 3, 4, 5]
C = [2, 1, 5, 3]
assert s.solve(A, B, C) == 1
