import multiprocessing
import time
from copy import deepcopy
from pprint import pformat


class Board(object):
    boards = None

    def __init__(self, board):
        self.iters = 0
        self.cols = 9
        self.candidates = {}
        self.cells = {}
        self._solved_board = None
        # log.debug(board)
        self.inprocess = False
        self._board = [list(map(int, line))
                       for line in [board[9 * i:9 * i + 9]
                                    for i in range(9)]]
        self.display(self._board)
        self.st = time.time()

    def get_candidates_for_cell(self, x, y, board):
        candidates = set(range(1, 10))
        for i in range(9):
            candidates.discard(board[i][y])
            candidates.discard(board[x][i])

        block_x = x // 3
        block_y = y // 3
        for i in range(3):
            for j in range(3):
                candidates.discard(
                    board[3 * block_x + i][3 * block_y + j])
        return candidates

    def display(self, board):
        print((pformat(board), self.iters))
        print((multiprocessing.current_process().pid))
        # render text

    #     for i in range(9):
    #         for j in range(9):
    #             if self._board[i][j]:
    #                 c = (255, 0, 0)
    #             else:
    #                 c = (0, 128, 0)
    #             text = font.render(str(board[i][j]), True, c)
    #             h = text.get_height() - 5
    #             textpos = text.get_rect()
    #             textpos.centerx = screen.get_rect().centerx + j * h - 200
    #             textpos.centery = 50 + i * h
    #             screen.fill((255, 255, 255), textpos)
    #             screen.blit(text, textpos)
    #     pygame.display.flip()

    def solve(self, job):
        board, depth = job
        self.iters += 1
        if self.iters % 100000 == 0:
            self.display(board)

        sorted_cands = []
        for i in range(9):
            for j in range(9):
                if board[i][j]:  # or self._board[i][j]:
                    continue
                cands = self.get_candidates_for_cell(i, j, board)
                sorted_cands.append((len(cands), i, j, cands))

        if not sorted_cands:
            self.display(board)
            self._solved_board = deepcopy(board)
            print(("------------------------", time.time() - self.st))
            return True

        r = sorted(sorted_cands)
        if r[0][0] == 0:
            return False

        i, j, cands = r[0][1:]

        jobs = []

        for cand in list(cands):

            board[i][j] = cand
            # self.display(board)

            jobs.append((deepcopy(board), depth + 1))

            if depth > 0:
                if self.solve((deepcopy(board), depth + 1)):
                    self.inprocess = False
                    return True

            board[i][j] = 0
            # self.display(board)

        if depth == 0:
            return jobs
