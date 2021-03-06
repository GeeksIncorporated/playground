# https://www.interviewbit.com/problems/valid-path/
# There is a rectangle with left bottom as  (0, 0) and right up as (x, y). There are N circles such that their centers are inside the rectangle.
# Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.
#
# Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.

class Solution:
    # @param A : x
    # @param B : y
    # @param C : N
    # @param D : R
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings

    seen_cells = {}

    def is_valid(self, cell):
        # to not recalculate many times
        if cell in self.seen_cells:
            return self.seen_cells[cell]
        x, y = cell
        for center in self.circle_centers:
            cx, cy = center
            if (cx - x) ** 2 + (cy - y) ** 2 < self.R ** 2:
                self.seen_cells[cell] = False
                return False
        self.seen_cells[cell] = True
        return True

    def get_valid_moves(self, cell):
        x, y = cell
        moves = set()
        for m in ((max(x - 1, 0), y),
                  (min(x + 1, self.A), y),
                  (x, max(0, y - 1)),
                  (x, min(self.B, y + 1)),
                  (max(x - 1, 0), max(y - 1, 0)),
                  (min(x + 1, self.A), max(y - 1, 0)),
                  (max(x - 1, 0), min(y + 1, self.B)),
                  (min(x + 1, self.A), min(y + 1, self.B))):
            if self.is_valid(m):
                moves.add(m)
        if cell in moves:
            moves.remove(cell)
        return moves

    def solve(self, A, B, C, R, E, F):
        self.A = A
        self.B = B
        self.R = R
        self.circle_centers = list(zip(E, F))
        visited = set()

        def dfs(cell, target):
            q = []
            q.append(cell)
            while q:
                cell = q.pop()
                if cell == target:
                    return True
                visited.add(cell)
                for adj in self.get_valid_moves(cell):
                    if adj not in visited:
                        q.append(adj)
            return False

        return "YES" if dfs((0, 0), (A, B)) else "NO"

A = 7
B = 91
C = 8
R = 7
E = [1,  7,  1,  7, 1, 5, 1, 6]
F = [25, 4, 74, 14, 90, 58, 37, 4]
s = Solution()
print(s.solve(A, B, C, R, E, F))
