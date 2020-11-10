import heapq
import pprint
import screen
import time
from copy import deepcopy, copy
import pygame
import sys

sys.setrecursionlimit(20240)
N = 9
H = []


def init_candidates(x, y, F):
    candidates = list(range(1, N + 1))
    for i in range(9):
        try:
            if F[i][y]:
                candidates.remove(F[i][y])
            if F[x][i]:
                candidates.remove(F[x][i])
        except:
            pass
    block_i = x // 3
    block_j = y // 3
    for i in range(3):
        for j in range(3):
            if F[3 * block_i + i][3 * block_j + j]:
                try:
                    candidates.remove(F[3 * block_i + i][3 * block_j + j])
                except:
                    pass
    return candidates


CELLS = {}


def init_heap(board):
    for x in range(9):
        for y in range(9):
            candidates = init_candidates(x, y, board)
            CELLS[(x, y)] = [len(candidates), (x, y), candidates]
            if not init_board[x][y]:
                heapq.heappush(H, CELLS[(x, y)])


def backtrack_cell(x, y):
    global init_board
    board[x][y] = init_board[x][y]


checked = 0


def display(board):
    # render text
    for i in range(9):
        for j in range(9):
            if init_board[i][j]:
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


pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
font = pygame.font.SysFont("serif", 30)


def increase_influence(x, y):
    for i in range(9):
        if i == x:
            continue

        if (board[x][y] not in CELLS[(i, y)][2]):
            CELLS[(i, y)][2].append(board[x][y])
            CELLS[(i, y)][0] = len(CELLS[(i, y)][2])
            if CELLS[(i, y)] not in H:
                heapq.heappush(H, CELLS[(i, y)])

        if (board[x][y] not in CELLS[(x, i)][2]):
            CELLS[(x, i)][2].append(board[x][y])
            CELLS[(x, i)][0] = len(CELLS[(x, i)][2])
            if CELLS[(x, i)] not in H:
                heapq.heappush(H, CELLS[(x, i)])
    block_i = x // 3
    block_j = y // 3
    for i in range(3):
        for j in range(3):
            if 3 * block_i + i == x or 3 * block_j + j == y:
                continue
            ti = 3 * block_i + i
            tj = 3 * block_j + j

            CELLS[(ti, tj)][2].append(board[x][y])
            CELLS[(ti, tj)][0] = len(CELLS[(ti, tj)][2])
            if CELLS[(ti, tj)] not in H:
                heapq.heappush(H, CELLS[(ti, tj)])

    heapq.heapify(H)


def decrease_influence(x, y):
    for i in range(9):
        if i == x:
            continue

        try:
            c = board[x][y]
            CELLS[(i, y)][2].remove(c)
            CELLS[(i, y)][0] = len(CELLS[(i, y)][2])
        except:
            pass

    for i in range(9):

        try:
            c = board[x][y]
            CELLS[(x, i)][2].remove(c)
            CELLS[(x, i)][0] = len(CELLS[(x, i)][2])
        except:
            pass

    block_i = x // 3
    block_j = y // 3
    for i in range(3):
        for j in range(3):
            ti = 3 * block_i + i
            tj = 3 * block_j + j
            if ti == x or tj == y:
                continue
            try:
                CELLS[(ti, tj)][2].remove(board[x][y])
                CELLS[(ti, tj)][0] = len(CELLS[(ti, tj)][2])
            except:
                pass
    heapq.heapify(H)


def is_complete():
    for i in range(9):
        for j in range(9):
            if not board[i][j]:
                return False
    return True


def is_valid(x, y, number):
    global board
    for i in range(N):
        if board[i][y] == number:
            return False

    for j in range(N):
        if board[x][j] == number:
            return False

    segment_x = x // 3  # 4 -> 1
    segment_y = y // 3  # 7 -> 2

    for i in range(segment_x * 3, segment_x * 3 + 3):
        for j in range(segment_y * 3, segment_y * 3 + 3):
            if board[i][j] == number:
                return False

    return True


VISITED = set()


def solve_sudoku(H):
    global checked
    while H:
        coords, candidates = heapq.heappop(H)[1:]
        x, y = coords

        for candidate in range(1, N+1):
            if not is_valid(x, y, candidate):
                continue
            print((CELLS[(2, 5)]))
            if init_board[x][y]:
                continue
            checked += 1
            board[x][y] = candidate
            display(board)
            # decrease_influence(x, y)

            if solve_sudoku(copy(H)):
                return 1

            # backtrack
            if board[x][y] and not init_board[x][y]:
                increase_influence(x, y)
                backtrack_cell(x, y)
                display(board)
    # solve_sudoku()
    return 0


boards = [
    # "000012300000400000105006700306000070700080009020000108001500403000001000003890000",
    # "000012300000300000104005600305000060600070002080000105001400903000001000003720000",
    "000012300000400000102003400305000040400060007020000106001800903000001000003670000",
    "000012300000400000103005600705000060600080009020000108001300807000001000007890000",
    "000012300000400000102005600305000060600070008020000107007900403000001000003280000",
    "000012300000400000105006700806000040700050009020000105001300408000001000008590000",
    "000012300000400000105006700306000070700080005050000108001200403000001000003890000",
    "000012300000400000105006200306000020200070008080000107001500403000001000003740000",
    "000031200000200000509008100201000070400090001090000804007900602000003000003560000",
    "000021800000600000501008300208000040100050007070000908009700604000009000002410000",
    "000012300000400000105006700306000070700020004080000102001500903000001000003290000",
    "000012300000400000105006700306000070700020004020000108004500903000001000003840000",
    "000024800000500000904007200608000020700010009040000705003700406000001000002350000",
    "000012300000400000105006700306000050700060008020000109001500802000001000003980000",
    "000012300000300000104005600607000010800030007040000205002700106000004000009160000",
    "000031600000200000903008400206000040400060009070000108009700501000002000007390000",
    "000031800000200000907005200302000040800050009070000108009700501000002000006390000",
    "000091800000400000908003100403000010100020008070000903009800604000009000004250000",
    "000029100000600000106005800401000090500080007060000503008400609000007000004860000",
    "000035900000100000605008200709000020500070003020000408003800509000009000004610000",
    "000034500000600000108009700309000070700080005050000108001400203000008000004290000",
    "000012300000400000105006700306000050700080009050000104001500903000004000003890000",
    "000031200000200000603008400208000050300060001070000806009700602000009000002510000",
    "000036200000200000506008400208000050300060001090000804009700602000003000003510000",
    "000012300000400000305006700806000050400070009030000402004300201000004000007920000",
    "000029100000100000106003700401000090500080006060000403007800604000007000008560000",
    "000012300000400000904005700406000020300060007050000106008700402000001000003680000",
    "000012300000300000104005200406000070700080009020000108001400903000001000003850000",
    "000012300000300000104005600305000060600070004080000107001200903000001000003740000",
    "000012300000300000104005600207000010800030002060000807003800109000003000002140000",
    "000012300000400000104005200607000080400070003080000504008500109000006000005320000",
    "000027600000900000802004500904000050500030008060000104001200809000008000009360000",
    "000012300000400000105006700306000040700020008080000109001500403000001000003980000",
    "000012300000300000204005600307000020800020009090000507006100408000008000001490000",
    "000012300000400000104005200305000020200060007080000106001700403000001000003690000",
    "000061700000500000406007300302000050500080001070000902009600408000009000003870000",
    "000012300000400000103005600705000060600070008020000107001300409000001000002780000",
    "000091400000700000503004900704000050900020001020000604006300507000006000007810000",
    "000054700000100000602003100906000010100030002040000508007800604000007000001940000",
    "000012300000400000102005600304000060600020007080000109001800402000001000003970000",
    "000012300000400000102005600407000080500040001060000702005100207000007000003820000",
    "000012300000300000405006100702000030600040008050000902008900604000003000007480000",
    "000012300000400000401003500602000030300050007070000805005600108000005000003780000",
    "000012300000400000501003600106000030700080006040000709009300208000006000004250000",
    "000012300000300000401005600605000010700080009020000704007600102000003000006920000",
    "000012300000400000305006800406000080200080007070000104008200405000003000007560000",
    "000031200000200000603008400208000040400050001070000908009300602000009000002510000",
    "000032500000400000605008400908000030300060004070000806009700602000009000004510000",
    "000028500000700000902005700403000070700010008050000603006200904000006000004150000",
    "000017500000200000702004600407000020300020005060000803004500901000009000008430000",
    "000012300000400000105006700701000080900040002080000906009300205000009000004120000",
    "000024700000500000307006200208000040900050006070000108009700601000009000005610000",
    "000075100000100000906004700401000020500030006060000403007800602000007000002560000",
    "000034700000500000304008200208000040900050006070000908009700601000009000005610000",
    "000012300000400000105006700701000020800040009030000806008300905000008000004190000",
    "000012300000400000402003100503000020600070004080000601006800209000006000007590000",
    "000012300000400000105006700706000020800050003090000806008300609000008000004560000",
    "000012300000400000506007100201000080800030007090000501008100706000008000004750000",
    "000012300000400000401005600705000010600020007030000806003600109000001000006590000",
    "000943000060010050000000000800000003750060014100000009000000000020050080000374000",
    "000123000040050060000000000700000003860040092900000001000000000050060080000392000",
    "000123000040050060000000000700000003860040072500000001000000000070060050000382000",
    "000123000040050060000000000500000007360040052700000001000000000080060040000732000",
    "000123000040050060000000000100000003760040082500000009000000000090060040000378000",
    "000123000040050060000000000700000003460080052500000001000000000090060040000392000",
    "000427000060090080000000000900000008120030045500000007000000000040060030000715000",
    "000123000040050060000000000200000003760040082400000001000000000080060030000372000",
    "000123000040050060000000000100000003360040052200000007000000000080060040000972000",
    "000123000040050060000000000800000007460080052200000001000000000050060040000731000",
    "000123000040050060000000000100000003760080052800000009000000000080060040000372000",
    "000651000040020080000000000700000009120030045800000001000000000030040020000719000",
    "000398000050010060000000000800000009120030045700000008000000000040020010000769000",
    "000123000040050060000000000200000003570040082100000006000000000060070040000392000",
    "000123000040050060000000000700000008810040027500000003000000000090060040000387000",
    "000123000040050060000000000400000003560040072700000001000000000080060040000372000",
    "000123000040050060000000000700000003460080052500000001000000000070060040000394000",
    "000123000040050060000000000200000007760040082300000001000000000090080040000376000",
    "000123000040050060000000000100000003560040072800000009000000000070060040000382000",
    "000427000010090080000000000700000005120030046800000002000000000040060090000715000",
    "000398000050020060000000000800000009620050041700000008000000000040060020000419000",
    "000123000040050060000000000500000003760040052400000001000000000080060040000372000",
    "000758000040060010000000000700000008120030045600000009000000000030010090000826000",
    "000123000040050060000000000100000003760080041800000009000000000080060090000372000",
    "000123000040050060000000000200000007360040052400000001000000000080060040000712000",
    "000123000040050060000000000100000003260070081900000002000000000080060040000294000",
    "000123000040050060000000000700000006360040082200000001000000000080060040000732000",
    "000123000040050010000000000200000006670040052800000003000000000050010040000862000",
    "000123000040050010000000000200000006630040072800000003000000000050010040000862000",
    "000123000040050060000000000500000003360040057700000001000000000080060040000237000",
    "000123000040050060000000000400000003760040052500000008000000000070090040000312000",
    "000123000040050060000000000200000007760040082500000001000000000090080040000372000",
    "000123000040050060000000000200000007760080092500000001000000000080060040000372000",
    "000123000040050060000000000200000007780040092500000001000000000050090040000372000",
    "000716000030050020000000000700000006120030045500000001000000000090040080000182000",
    "010020300004005060070000008006900070000100002030048000500006040000800106008000000",
    "010020300002003040050000006004700050000100003070068000300004090000600104006000000",
    "010020300002003040080000006004700030000600008070098000300004090000800104006000000",
    "010020300002003040050000006004200050000100007020087000300004080000600105006000000",
    "010020300002003040050000006004700050000100008070098000300004090000900804006000000",
    "010020300004003020050000006002700050000100008070098000300007090000600102007000000",
    "010020300002003040050000006004700050000100008070038000300005090000600104006000000",
    "010020300004001050060000007005400060000100002080092000300005090000700106007000000",
    "010020300003004050060000007005800060000100009080092000400005090000700106007000000",
    "010020300004003050050000006005700040000100002070082000300005090000600105006000000",
    "010020300002003040050000006004700050000100008070068000300004060000500104009000000",
    "010020300002003040050000006004700050000100008070095000300004090000900104006000000",
    "010020300004005060070000008006300070000100002030092000900006040000800106008000000",
    "080070100003002090060000004009500060000700005020041000100005020000200901004000000",
    "010020300002003040040000006004700050000600008070098000300005080000800104009000000",
    "020010700003008060010000003008600050000900004030021000400009080000500901007000000",
    "010020300003004050060000007005800060000100002080072000400005090000700104007000000",
    "010020300002003040050000006007800050000100004080094000300007090000400105006000000",
    "010020300004003020050000006007600050000100002060072000300008070000900108009000000",
    "010020300004003050060000007005800060000900001080012000300005010000700506002000000",
    "010020300004003050020000006005700020000100008070098000300005090000900205006000000",
    "010020300004003020050000006007800050000100002080042000300007040000600807006000000",
    "070050800005008020010000009008100050000200001090034000900002030000600107006000000",
    "010020300004005060070000004006800070000900002050017000400006050000400906008000000",
    "010020300004005060070000008006900080000100002090032000200006030000800105008000000",
    "010020300002003040050000006004700050000100008070098000200004090000600704006000000",
    "010020300002003040050000006004700050000100008070068000300004090000800104006000000",
    "010020300004001050060000007005800070000900002080014000300005010000700905007000000",
    "010020300004003020050000006002700050000800009070019000300002010000600805006000000",
    "010020300003004050060000007008900070000100002090082000200005080000700105007000000",
    "010020300004003050020000006007800040000100005080095000300007090000600107006000000",
    "010020300002003040050000006004700080000100003070068000300004090000600104006000000",
    "090020500004005010060000003001800060000900002080072000500001070000300901003000000",
    "010020300004001050060000007005800060000100003080092000300005090000700102007000000",
    "010020300002003040050000006004700050000100008020098000700004090000600104006000000",
    "010020300003004050060000004005700060000100002070032000400005080000900105009000000",
    "010020300004003050060000007005800040000100002080092000600005090000700105002000000",
    "010020300004003050060000007005100060000800002080092000300006090000700205007000000",
    "010020300004005060070000008006900030000100002090042000500006040000800106008000000",
    "010020300004003050060000007005200060000100008020048000300005090000700205009000000",
    "070040800009005060060000003004100070000200006020034000100008090000600401007000000",
    "010020300004003050060000007005200040000800001020091000300005090000700805007000000",
    "010020300004001050060000007005200060000800009020019000300005010000700805007000000",
    "010020300004001050060000007005800060000900002080014000300005010000700905007000000",
    "010020300004003050060000007005800060000100002070092000400005090000700105007000000",
    "010020300004005060050000004006700040000100002070082000300006080000900106009000000",
    "010020300004003050020000006005700080000100002070098000800005090000600105006000000",
    "010020300004003050060000007005800040000100008080092000300005090000700605007000000",
    "010020300004005060070000008006900040000100002090032000500006030000800906008000000",
    "010020300004003050060000007005800060000100002070092000300005090000700105007000000",
    "010020300002003040050000006004700050000600008070098000300004090000800104006000000",
    "010020300004003050060000007005800060000100009080042000300005040000700908001000000",
    "070060900006002030020000006003100040000200008050034000900003020000700105008000000",
    "010020300004003050060000001005700060000800002070012000400005090000400805007000000",
    #
    # "400006000060000009000000000002000000000000000003060020100000900800005000000000005",
    # "400000805030000000000700000020000060000080400000010000000603070500200000104000000",
    # "520006000000000701300000000000400800600000050000000000041800000000030020008700000",
    # "600000803040700000000000000000504070300200000106000000020000050000080600000010000",
    # "480300000000000071020000000705000060000200800000000000001076000300000400000050000",
    # "000014000030000200070000000000900030601000000000000080200000104000050600000708000",
    # "000000520080400000030009000501000600200700000000300000600010000000000704000000030",
    # "602050000000003040000000000430008000010000200000000700500270000000000081000600000",
    # "052400000000070100000000000000802000300000600090500000106030000000000089700000000",
    # "602050000000004030000000000430008000010000200000000700500270000000000081000600000",
    # "092300000000080100000000000107040000000000065800000000060502000400000700000900000",
    # "600302000050000010000000000702600000000000054300000000080150000000040200000000700",
    # "060501090100090053900007000040800070000000508081705030000050200000000000076008000",
    # "005000987040050001007000000200048000090100000600200000300600200000009070000000500",
    # "306070000000000051800000000010405000700000600000200000020000040000080300000500000",
    # "100000308070400000000000000203010000000000095800000000050600070000080200040000000",
    # "600302000040000010000000000702600000000000054300000000080150000000040200000000700",
    # "000030090000200001050900000000000000102080406080500020075000000401006003000004060",
    # "450000030000801000090000000000050090200700000800000000010040000000000702000600800",
    # "023700006800060590900000700000040970307096002000000000500470000000002000080000000",
    # "008400030000300000900001574790008000000007005140000020009060002050000400000090056",
    # "098010000200000060000000000000302050084000000000600000000040809300500000000000100",
    # "002470058000000000000001040000020009528090400009000100000000030300007500685002000",
    # "400000805030000000000700000020000060000050400000010000000603070500200000109000000",
    # "020300000063000005800000001500009030000700000000100008087900260000006070006007004",
    # "100000709040007200800000000070010060300000005060040020000000008005300070702000046",
    # "400000300000802000000700000000100087340000000600000000500060000000010400082000000",
    # "000000071020800000000403000700060050000200300900000000600070000080000400000050000",
    # "600302000040000080000000000702600000000000054300000000080150000000080200000000700",
    # "047080001000000000000600700600003570000005000010060000280040000090100040000020690",
    # "000000801700200000000506000000700050010000300080000000500000020040080000600030000",
    # "380600000009000000020030510000005000030010060000400000017050080000000900000007032",
    # "000500000000000506970000020004802000250100030080030000000004070013050090020003100",
    # "020000000305062009068000300050000000000640802004700900003000001000006000170430000",
    # "080040000300000010000000020005000406900100800200000000000309000060000500000200000",
    # "008090100060500020000006000030107050000000009004000300050000200070003080200700004",
    # "400000508030000000000700000020000060000050800000010000000603070500200000108000000",
    # "100000308060400000000000000203010000000000095800000000050600070000080200040000000",
    # "100006080064000000000040007000090600070400500500070100050000320300008000400000000",
    # "249060003030000200800000005000006000000200000010040820090500700004000001070003000",
    # "000800009087300040600700000008500970000000000043007500000003000030001450400002001",
    # "000501000090000800060000000401000000000070090000000030800000105000200400000360000",
    # "000000801600200000000705000000600020010000300080000000200000070030080000500040000",
    # "047600050803000002000009000000805006000100000602400000078000510006000040090004007",
    # "000007095000001000860020000020073008500000060003004900305000417240000000000000000",
    # "040500000800090030076020000014600000000009007000003600001004050060000003007100200",
    # "083400000000070050000000000040108000000000027000300000206050000500000800000000100",
    # "009000003000009000700000506006500400000300000028000000300750600600000000000120308",
    # "026039000000600001900000700000004009050000200008500000300200900400007620000000004",
    # "203080000800700000000000100060507000400000030000100000000000082050000600010000000",
    # "600302000010000050000000000702600000000000084300000000080150000000080200000000700",
    # "100000900064001070070040000000300000308900500007000020000060709000004010000129030",
    # "000000000900000084062300050000600045300010006000900070000100000405002000030800009",
    # "020000593800500460940060008002030000060080730700200000000040380070000600000000005",
    # "904005000250600100310000008070009000400260000001470000700000002000300806040000090",
    # "000520000090003004000000700010000040080045300600010008702000000008000032040080010",
    # "530020900024030050009000000000010827000700000000098100000000000006400009102050430",
    # "100007860007008010800200009000000002400010000009005000608000000000050900000009304",
    # "000050001100000070060000080000004000009010300000596020080062007007000000305070200",
    # "047020000800001000030000902000005000600810050000040000070000304000900010400270800",
    # "000000940000090005300005070080400100463000000000007080800700000700000028050260000",
    # "020000006000041000007800001000000700003700000600412000010074005008050070000003900",
    # "100000308060400000000000000203010000000000075800000000070500060000080200040000000",
    # "200001090010030700900800020000000850060400000000070003020300060000500000109000205",
    # "007008000006020300030000009010050060000010000070900002000000004083004000260000510",
    # "000360000850000000904008000000006800000000017009004500010500060400009002000003000",
    # "340600000007000000020080570000005000070010020000400000036020010000000900000007082",
    # "000000401800200000000607000000800060040000300010000000600000020050010000700030000",
    # "040050067000100040000200000100800300000000200060000000000040050300000800200000000",
    # "000000040002004001070050090003007000040060000600100800020000100850900060000080003",
    # "800700004050000600000000000030970008000043005000020900006000000200060007071008302",
    # "080004050000700300000000000010085000600000200000040000302600000000000041700000000",
    # "000070080006000500020003061010007002008005340200900000002000000580006030400010000",
    # "000000801600200000000705000000600020010000300080000000200000070040080000500030000",
    # "020000000000600003074080000000003002080040010600500000000010780500009000000000040",
    # "052006800000007020000000600004800900200410000001000008006100380000090006300600109",
    # "000010780500009000000000040020000000000600003074080000000003002080040010600500000",
    # "100000003060300700070005001210700090007000000008010020000806400009020060000400000",
    # "400070100001904605000001000000700002002030000847006000014000806020000300600090000",
    # "000000801700200000000506000000700050010000300080000000500000020030080000600040000",
    # "963000000100008000000205000040800000010000700000030025700000030009020407000000900",
    # "150300000070040200004072000008000000000900108010080790000003800000000000600007423",
    # "000000000057240009800009470009003000500900120003010900060000250000560000070000006",
    # "000075000010020000040003000500000302000800010000000600000100480200000000700000000",
    # "600000703040800000000000000000504080700200000103000000020000050000070900000010000",
    # "000060004006030000100400507700000805000800000608000090002090000400003200009700100",
    # "032000005800300000904280001000400039000600050000010000020006708000004000095000060",
    # "000503000000060700508000016360020000000401000000030005670000208004070000000200500",
    # "050307040100000000030000000508030610000800509060010000000040006000692700002000900",
    # "005008001800000090000000780000400000640000900000053002060000000001380050000907140",
    # "000000000072060100005100082080001300400000000037090010000023800504009000000000790",
    # "000658000004000000120000000000009607000300500002080003001900800306000004000047300",
    # "020300000006008090830500000000200080709005000000006004000000010001000402200700809",
    # "050090000100000600000308000008040009514000000030000200000000004080006007700150060",
    # "000002000000070001700300090800700000020890600013006000090050824000008910000000000",
    # "300080000000700005100000000000000360002004000070000000000060130045200000000000800"
    "071840009026009000000106054082000007750000048100000920810507000000600130600013780",
    "000260701680070090190004500820100040004602900050003028009300074040050036703018000",
    "310004069000000200008005040000000005006000017807030000590700006600003050000100002",
    "200080300060070084030500209000105408000000000402706000301007040720040060004010003",
    "000000907000420180000705026100904000050000040000507009920108000034059000507000000",
    "030050040008010500460000012070502080000603000040109030250000098001020600080060020",
    "020810740700003100090002805009040087400208003160030200302700060005600008076051090",
    "100920000524010000000000070050008102000000000402700090060000000000030945000071006",
    "043080250600000000000001094900004070000608000010200003820500000000000005034090710",
    "480006902002008001900370060840010200003704100001060049020085007700900600609200018",
    "000900002050123400030000160908000000070000090000000205091000050007439020400007000",
    "001900003900700160030005007050000009004302600200000070600100030042007006500006800",
    "000125400008400000420800000030000095060902010510000060000003049000007200001298000",
    "062340750100005600570000040000094800400000006005830000030000091006400007059083260",
    "300000000005009000200504000020000700160000058704310600000890100000067080000005437",
    "630000000000500008005674000000020000003401020000000345000007004080300902947100080",
    "000020040008035000000070602031046970200000000000501203049000730000000010800004000",
    "361025900080960010400000057008000471000603000259000800740000005020018060005470329",
    "050807020600010090702540006070020301504000908103080070900076205060090003080103040",
    "080005000000003457000070809060400903007010500408007020901020000842300000000100080",
    "003502900000040000106000305900251008070408030800763001308000104000020000005104800",
    "000000000009805100051907420290401065000000000140508093026709580005103600000000000",
    "020030090000907000900208005004806500607000208003102900800605007000309000030020050",
    "005000006070009020000500107804150000000803000000092805907006000030400010200000600",
    "040000050001943600009000300600050002103000506800020007005000200002436700030000040",
    "004000000000030002390700080400009001209801307600200008010008053900040000000000800",
    "360020089000361000000000000803000602400603007607000108000000000000418000970030014",
    "500400060009000800640020000000001008208000501700500000000090084003000600060003002",
    "007256400400000005010030060000508000008060200000107000030070090200000004006312700",
    "000000000079050180800000007007306800450708096003502700700000005016030420000000000",
    "030000080009000500007509200700105008020090030900402001004207100002000800070000090",
    "200170603050000100000006079000040700000801000009050000310400000005000060906037002",
    "000000080800701040040020030374000900000030000005000321010060050050802006080000000",
    "000000085000210009960080100500800016000000000890006007009070052300054000480000000",
    "608070502050608070002000300500090006040302050800050003005000200010704090409060701",
    "050010040107000602000905000208030501040070020901080406000401000304000709020060010",
    "053000790009753400100000002090080010000907000080030070500000003007641200061000940",
    "006080300049070250000405000600317004007000800100826009000702000075040190003090600",
    "005080700700204005320000084060105040008000500070803010450000091600508007003010600",
    "000900800128006400070800060800430007500000009600079008090004010003600284001007000",
    "000080000270000054095000810009806400020403060006905100017000620460000038000090000",
    "000602000400050001085010620038206710000000000019407350026040530900020007000809000",
    "000900002050123400030000160908000000070000090000000205091000050007439020400007000",
    "380000000000400785009020300060090000800302009000040070001070500495006000000000092",
    "000158000002060800030000040027030510000000000046080790050000080004070100000325000",
    "010500200900001000002008030500030007008000500600080004040100700000700006003004050",
    "080000040000469000400000007005904600070608030008502100900000005000781000060000010",
    "904200007010000000000706500000800090020904060040002000001607000000000030300005702",
    "000700800006000031040002000024070000010030080000060290000800070860000500002006000",
    "001007090590080001030000080000005800050060020004100000080000030100020079020700400",
    "000003017015009008060000000100007000009000200000500004000000020500600340340200000",
    "300200000000107000706030500070009080900020004010800050009040301000702000000008006"]

boards = ["000000520080400000030009000501000600200700000000300000600010000000000704000000030",]
if __name__ == "__main__":
    for board in boards:
        board = [list(map(int, list(line))) for line in
                 [board[i:i + N] for i in range(0, len(board), N)]]
        init_board = deepcopy(board)
        init_heap(init_board)
        print("SUDOKU PUZZLE:")
        pprint.pprint(board)
        st = time.time()
        solve_sudoku()
        pprint.pprint(board)
        print(("Took", time.time() - st, "sec"))
        print(("Numbers tried:", checked))
        time.sleep(1)
