# https://www.interviewbit.com/problems/word-search-board/
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The cell itself does not count as an adjacent cell.
# The same letter cell may be used more than once.
#
# Example :
#
# Given board =
#
# [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
# ]
# word = "ABCCED", -> returns 1,
# word = "SEE", -> returns 1,
# word = "ABCB", -> returns 1,
# word = "ABFSAB" -> returns 1
# word = "ABCD" -> returns 0
# Note that 1 corresponds to true, and 0 corresponds to false.

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer

    def get_adjs(self, A, cell):
        i, j = cell
        s = set([
            (max(i - 1, 0), j),
            (i, max(j - 1, 0)),
            (min(i + 1, len(A) - 1), j),
            (i, min(j + 1, len(A[0])- 1))
        ])
        if (i, j) in s:
            s.remove((i, j))
        return s

    def exist(self, A, B):

        def dfs(postfix, cell):

            if len(postfix) == 0:
                return True

            for adj in self.get_adjs(A, cell):
                if A[adj[0]][adj[1]] == postfix[0]:
                    if dfs(postfix[1:], adj):
                        return True

        postfix = B
        for i in range(len(A)):
            for j in range(len(A[0])):
                if postfix[0] == A[i][j]:
                    if dfs(postfix[1:], (i, j)):
                        return 1
        return 0


A = ["FEDCBECD",
     "FABBGACG",
     "CDEDGAEC",
     "BFFEGGBA",
     "FCEEAFDA",
     "AGFADEAC",
     "ADGDCBAA",
     "EAABDDFF"]

B = "BCDCB"

s = Solution()
print(s.exist(A, B))
assert s.exist(A, B) == 1


A = ["FFAGCA",
     "EFCAEC",
     "CCFDGD",
     "DEGEBB",
     "CGAEEC",
     "GBDFGE",
     "CBBGBA",
     "GFGAAF",
     "FGGEFE",
     "GCBBFD"]

B = "CDCBAECDF"
s = Solution()
print(s.exist(A, B))
assert s.exist(A, B) == 0
