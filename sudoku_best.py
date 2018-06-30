# -*-coding:utf8;-*-
from copy import deepcopy
from collections import defaultdict
import time
import threading
import pygame
import heapq

H = []
Hs = set()

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
font = pygame.font.SysFont("serif", 30)


class Cell(object):

    def __init__(self, x, y, cands):
        self.x = x
        self.y = y
        self.cands = cands

    def __repr__(self):
        return " ".join(map(str, [self.x, self.y, self.cands]))

    def __cmp__(self, B):
        if len(self.cands) > len(B.cands):
            return 1
        elif len(self.cands) == len(B.cands):
            return 0
        else:
            return -1

class Board(object):
    boards = None

    def __init__(self, board):
        super(Board, self).__init__()
        self.cols = 9
        self.inprocess = False
        self.opened_nums = board.count('0')
        self._board = [map(int, line)
                       for line in [board[9 * i:9 * i + 9]
                                    for i in range(9)]]
        print(str(self._board))
        self._init_candidates()
        self.display(self._board)

    def display(self, board):
        # render text
        for i in range(9):
            for j in range(9):
                if self._board[i][j]:
                    c = (255, 0, 0)
                else:
                    c = (0, 128, 0)
                text = font.render(str(board[i][j]), True, c)
                h = text.get_height() - 5
                textpos = text.get_rect()
                textpos.centerx = screen.get_rect().centerx + j * h - 200
                textpos.centery = 50 + i * h

                screen.fill((255, 255, 255), textpos)
                screen.blit(text, textpos)
        pygame.display.flip()

    def _init_candidates(self):
        self.cands = defaultdict(dict)
        for i in range(9):
            for j in range(9):
                if self._board[i][j]:
                    continue
                cands = self.get_candidates_for_cell(i, j, self._board)
                self.cands[i][j] = Cell(i, j, cands)
                heapq.heappush(H, self.cands[i][j])
                Hs.add((i,j))

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

    def eliminate_cand(self, x, y, cand, board):
        print(str(['--', x, y, cand]))
        for i in range(9):
            if board[i][y]:
                continue
            self.cands[i][y].cands.discard(cand)
            if not len(self.cands[i][y].cands) and \
                (i, y) in Hs:
                Hs.discard((i, y))
                H.remove(self.cands[i][y])

        for i in range(9):
            if self._board[x][i]:
                continue
            self.cands[x][i].cands.discard(cand)

            if not len(self.cands[x][i].cands) \
                and (x, i) in Hs:
                H.remove(self.cands[x][i])
                Hs.discard((x, i))

        block_x = x // 3
        block_y = y // 3
        for i in range(3):
            for j in range(3):
                if board[3 * block_x + i][3 * block_y + j]:
                    continue
                self.cands[3 * block_x + i][3 * block_y + j].cands.discard(cand)
                if not len(self.cands[3 * block_x + i][3 * block_y + j].cands) \
                    and (3 * block_x + i, 3 * block_y + j) in Hs:
                    H.remove(self.cands[3 * block_x + i, 3 * block_y + j])
                    Hs.discard((3 * block_x + i, 3 * block_y + j))

        heapq.heapify(H)
        print(sorted(map(str, H)))

    def restore_cand(self, x, y, cand, board):
        print(str(['++', x, y, cand]))

        for i in range(9):
            if board[i][y] or i == x:
                print(1)
                continue

            self.cands[i][y].cands.add(cand)
            if (i, y) not in Hs:
                print("_---------_%s,%s" % (self.cands[i][y], str(Hs)))
                H.append(self.cands[i][y])
                Hs.add((i, y))

        for i in range(9):
            if board[x][i] or i == y:
                continue

            self.cands[x][i].cands.add(cand)

            if (x, i) not in Hs:
                H.append(self.cands[x][i])
                Hs.add((x, i))

        block_x = x // 3
        block_y = y // 3
        for i in range(3):
            for j in range(3):
                if board[3 * block_x + i][3 * block_y + j]:
                    continue

                self.cands[3 * block_x + i][3 * block_y + j].cands.add(cand)

                if (3 * block_x + i, 3 * block_y + j) not in Hs:
                    H.append(self.cands[3 * block_x + i][3 * block_y + j])
                    Hs.add((3 * block_x + i, 3 * block_y + j))

        heapq.heapify(H)
        print(sorted(map(str,H)))

    def is_valid(self, x, y, number, board):
        for i in range(9):
            if board[i][y] == number:
                return False

        for j in range(9):
            if board[x][j] == number:
                return False

        segment_x = x // 3  # 4 -> 1
        segment_y = y // 3  # 7 -> 2

        for i in range(segment_x * 3, segment_x * 3 + 3):
            for j in range(segment_y * 3, segment_y * 3 + 3):
                if board[i][j] == number:
                    return False

        return True

    def solve(self, board, depth):
        print("0*** %s", depth)

        if not len(H):
            if depth == self.opened_nums:
                time.sleep(5)
                return True
            return False

        # r = sorted(H)[depth]
        r = heapq.heappop(H)
        i = r.x
        j = r.y
        cands = r.cands
        print(str(['@@', i, j, cands]))

        for cand in list(cands):
            if not self.is_valid(i, j, cand, board):
                continue
            board[i][j] = cand
            self.display(board)
            self.eliminate_cand(i, j, cand, board)

            if self.solve(deepcopy(board), depth + 1):
                self.inprocess = False
                return True
            board[i][j] = 0
            self.restore_cand(i, j, cand, board)
            self.display(board)
        Hs.discard((i, j))

    def on_touch_down(self, touch):
        if self.inprocess:
            return
        self.inprocess = True

        threading.Thread(
            target=self.solve, args=(
                deepcopy(self._board), 0)).start()



boards = [
    # "400006000060000009000000000002000000000000000003060020100000900800005000000000005",
    "400000805030000000000700000020000060000080400000010000000603070500200000104000000",
    "520006000000000701300000000000400800600000050000000000041800000000030020008700000",
    "600000803040700000000000000000504070300200000106000000020000050000080600000010000",
    "480300000000000071020000000705000060000200800000000000001076000300000400000050000",
    "000014000030000200070000000000900030601000000000000080200000104000050600000708000",
    "000000520080400000030009000501000600200700000000300000600010000000000704000000030",
    "602050000000003040000000000430008000010000200000000700500270000000000081000600000",
    "052400000000070100000000000000802000300000600090500000106030000000000089700000000",
    "602050000000004030000000000430008000010000200000000700500270000000000081000600000",
    "092300000000080100000000000107040000000000065800000000060502000400000700000900000",
    "600302000050000010000000000702600000000000054300000000080150000000040200000000700",
    "060501090100090053900007000040800070000000508081705030000050200000000000076008000",
    "005000987040050001007000000200048000090100000600200000300600200000009070000000500",
    "306070000000000051800000000010405000700000600000200000020000040000080300000500000",
    "100000308070400000000000000203010000000000095800000000050600070000080200040000000",
    "600302000040000010000000000702600000000000054300000000080150000000040200000000700",
    "000030090000200001050900000000000000102080406080500020075000000401006003000004060",
    "450000030000801000090000000000050090200700000800000000010040000000000702000600800",
    "023700006800060590900000700000040970307096002000000000500470000000002000080000000",
    "008400030000300000900001574790008000000007005140000020009060002050000400000090056",
    "098010000200000060000000000000302050084000000000600000000040809300500000000000100",
    "002470058000000000000001040000020009528090400009000100000000030300007500685002000",
    "400000805030000000000700000020000060000050400000010000000603070500200000109000000",
    "020300000063000005800000001500009030000700000000100008087900260000006070006007004",
    "100000709040007200800000000070010060300000005060040020000000008005300070702000046",
    "400000300000802000000700000000100087340000000600000000500060000000010400082000000",
    "000000071020800000000403000700060050000200300900000000600070000080000400000050000",
    "600302000040000080000000000702600000000000054300000000080150000000080200000000700",
    "047080001000000000000600700600003570000005000010060000280040000090100040000020690",
    "000000801700200000000506000000700050010000300080000000500000020040080000600030000",
    "380600000009000000020030510000005000030010060000400000017050080000000900000007032",
    "000500000000000506970000020004802000250100030080030000000004070013050090020003100",
    "020000000305062009068000300050000000000640802004700900003000001000006000170430000",
    "080040000300000010000000020005000406900100800200000000000309000060000500000200000",
    "008090100060500020000006000030107050000000009004000300050000200070003080200700004",
    "400000508030000000000700000020000060000050800000010000000603070500200000108000000",
    "100000308060400000000000000203010000000000095800000000050600070000080200040000000",
    "100006080064000000000040007000090600070400500500070100050000320300008000400000000",
    "249060003030000200800000005000006000000200000010040820090500700004000001070003000",
    "000800009087300040600700000008500970000000000043007500000003000030001450400002001",
    "000501000090000800060000000401000000000070090000000030800000105000200400000360000",
    "000000801600200000000705000000600020010000300080000000200000070030080000500040000",
    "047600050803000002000009000000805006000100000602400000078000510006000040090004007",
    "000007095000001000860020000020073008500000060003004900305000417240000000000000000",
    "040500000800090030076020000014600000000009007000003600001004050060000003007100200",
    "083400000000070050000000000040108000000000027000300000206050000500000800000000100",
    "009000003000009000700000506006500400000300000028000000300750600600000000000120308",
    "026039000000600001900000700000004009050000200008500000300200900400007620000000004",
    "203080000800700000000000100060507000400000030000100000000000082050000600010000000",
    "600302000010000050000000000702600000000000084300000000080150000000080200000000700",
    "100000900064001070070040000000300000308900500007000020000060709000004010000129030",
    "000000000900000084062300050000600045300010006000900070000100000405002000030800009",
    "020000593800500460940060008002030000060080730700200000000040380070000600000000005",
    "904005000250600100310000008070009000400260000001470000700000002000300806040000090",
    "000520000090003004000000700010000040080045300600010008702000000008000032040080010",
    "530020900024030050009000000000010827000700000000098100000000000006400009102050430",
    "100007860007008010800200009000000002400010000009005000608000000000050900000009304",
    "000050001100000070060000080000004000009010300000596020080062007007000000305070200",
    "047020000800001000030000902000005000600810050000040000070000304000900010400270800",
    "000000940000090005300005070080400100463000000000007080800700000700000028050260000",
    "020000006000041000007800001000000700003700000600412000010074005008050070000003900",
    "100000308060400000000000000203010000000000075800000000070500060000080200040000000",
    "200001090010030700900800020000000850060400000000070003020300060000500000109000205",
    "007008000006020300030000009010050060000010000070900002000000004083004000260000510",
    "000360000850000000904008000000006800000000017009004500010500060400009002000003000",
    "340600000007000000020080570000005000070010020000400000036020010000000900000007082",
    "000000401800200000000607000000800060040000300010000000600000020050010000700030000",
    "040050067000100040000200000100800300000000200060000000000040050300000800200000000",
    "000000040002004001070050090003007000040060000600100800020000100850900060000080003",
    "800700004050000600000000000030970008000043005000020900006000000200060007071008302",
    "080004050000700300000000000010085000600000200000040000302600000000000041700000000",
    "000070080006000500020003061010007002008005340200900000002000000580006030400010000",
    "000000801600200000000705000000600020010000300080000000200000070040080000500030000",
    "020000000000600003074080000000003002080040010600500000000010780500009000000000040",
    "052006800000007020000000600004800900200410000001000008006100380000090006300600109",
    "000010780500009000000000040020000000000600003074080000000003002080040010600500000",
    "100000003060300700070005001210700090007000000008010020000806400009020060000400000",
    "400070100001904605000001000000700002002030000847006000014000806020000300600090000",
    "000000801700200000000506000000700050010000300080000000500000020030080000600040000",
    "963000000100008000000205000040800000010000700000030025700000030009020407000000900",
    "150300000070040200004072000008000000000900108010080790000003800000000000600007423",
    "000000000057240009800009470009003000500900120003010900060000250000560000070000006",
    "000075000010020000040003000500000302000800010000000600000100480200000000700000000",
    "600000703040800000000000000000504080700200000103000000020000050000070900000010000",
    "000060004006030000100400507700000805000800000608000090002090000400003200009700100",
    "032000005800300000904280001000400039000600050000010000020006708000004000095000060",
    "000503000000060700508000016360020000000401000000030005670000208004070000000200500",
    "050307040100000000030000000508030610000800509060010000000040006000692700002000900",
    "005008001800000090000000780000400000640000900000053002060000000001380050000907140",
    "000000000072060100005100082080001300400000000037090010000023800504009000000000790",
    "000658000004000000120000000000009607000300500002080003001900800306000004000047300",
    "020300000006008090830500000000200080709005000000006004000000010001000402200700809",
    "050090000100000600000308000008040009514000000030000200000000004080006007700150060",
    "000002000000070001700300090800700000020890600013006000090050824000008910000000000",
    "300080000000700005100000000000000360002004000070000000000060130045200000000000800"]
# boards = [
#     "071840009026009000000106054082000007750000048100000920810507000000600130600013780"]

if __name__ == '__main__':
    for b in boards:
        board = Board(b)
        board.solve(deepcopy(board._board), depth=0)