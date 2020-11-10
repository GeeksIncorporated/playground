from queue import Queue


class Solution:
    # @param N : integer
    # @param M : integer
    # @param x1 : integer
    # @param y1 : integer
    # @param x2 : integer
    # @param y2 : integer
    # @return an integer

    def get_possible_moves(self, N, M, cell):
        i, j = cell
        moves = []
        for m in [
            (i - 2, j - 1),
            (i - 2, j + 1),
            (i + 2, j - 1),
            (i + 2, j + 1),
            (i - 1, j - 2),
            (i - 1, j + 2),
            (i + 1, j - 2),
            (i + 1, j + 2)]:
            if (m[0] > 0 and m[0] <= N) and (m[1] > 0 and m[1] <= M):
                moves.append(m)
        return moves

    def knight(self, N, M, x1, y1, x2, y2):

        def bfs(cell, end):
            q = Queue()
            q.put((0, cell))
            visited = set()
            while not q.empty():
                d, cell = q.get()
                if cell == end:
                    return d

                visited.add(cell)
                d += 1
                for move in self.get_possible_moves(N, M, cell):
                    if move in visited:
                        continue
                    q.put((d, move))
            return -1

        return bfs((x1, y1), (x2, y2))


N = 8
M = 8
x1 = 1
y1 = 1
x2 = 8
y2 = 8

s = Solution()
print((s.knight(N, M, x1, y1, x2, y2)))

N = 2
M = 20
x1 = 1
y1 = 18
x2 = 1
y2 = 5

s = Solution()
print((s.knight(N, M, x1, y1, x2, y2)))
