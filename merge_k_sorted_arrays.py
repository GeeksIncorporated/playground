import heapq


class A:
    def __init__(self):
        self.a = 1
        
class B(A):
    def __init__(self):
        super(B, self).__init__()


class Solution:
    
    def mergeKLists(self, lists):
        h = []
        for l in lists:
            heapq.heappush(h, l)
        res = []

        while h:
            smallest_list = heapq.heappop(h)
            if not smallest_list:
                continue
            res.append(smallest_list[0])
            heapq.heappush(h, smallest_list[1:])

        return res


s = Solution()
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
r = s.mergeKLists(lists)
print(r)
