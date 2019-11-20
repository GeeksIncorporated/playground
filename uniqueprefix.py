import itertools


class Solution:
    prefix_tree = {}

    def build_prefix_tree(self, word):
        node = self.prefix_tree
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        return node

    def get_unique_prefix(self, word):
        uniq_prefix = []
        node = self.prefix_tree

        def solve(node, i):
            uniq_prefix.append(word[i])
            node = node[word[i]]
            if not node:
                return 0
            childs = max(len(node), solve(node, i+1))
            if childs == 1:
                uniq_prefix.pop()
            return childs
        solve(node, 0)
        return uniq_prefix


    def prefix(self, A):

        for word in A:
            self.build_prefix_tree(word)

        res = []
        for word in A:
            prefix = self.get_unique_prefix(word)
            res.append("".join(prefix))
        return res

s = Solution()
print s.prefix(["v", "rr", "lj", "tnsnfwzqfj", "afadr", "wsofsbcnuv", "hffbsaq", "wp", "cb", "cehch"])



