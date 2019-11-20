class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        global_res = []
        i = 0
        while i < len(A)-1:
            local_res = []
            for j in range(i, len(A)):
                print(i, j)
                if A[j] >= 0:
                    local_res.append(A[j])
                else:
                    i = j
                    global_res.append((sum(local_res),len(local_res), -j, local_res))
                    break
            i += 1

        if local_res:
            global_res.append((sum(local_res),len(local_res), -j, local_res))
        if not global_res:
            return []
        return sorted(global_res, reverse=True)[0][3]

s = Solution()
print(s.maxset([ 1, 2, 5, -7, 2, 5 ]))
print(s.maxset([ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]))
print(s.maxset([ -317097467, 1376710097, 1330573317, 1687926652 ]))