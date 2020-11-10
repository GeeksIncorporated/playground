import time


class Solution:

    def minRemoveToMakeValid(self, s):
        stack = []
        indeces_to_remove = set()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    indeces_to_remove.add(i)
                else:
                    stack.pop()
        while stack:
            indeces_to_remove.add(stack.pop())

        result = []
        for i in range(len(s)):
            if i in indeces_to_remove:
                continue
            result.append(s[i])
        return "".join(result)

s = Solution()
st = time.time()
r = s.minRemoveToMakeValid(
    "a(sdf))(as()asd")
print(time.time() - st)
print(r)
