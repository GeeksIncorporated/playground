#
# You are given 3 arrays A, B and C. All 3 of the arrays are sorted.
#
# Find i, j, k such that :
# max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
# Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
#
# **abs(x) is absolute value of x and is implemented in the following manner : **
#
#       if (x < 0) return -x;
#       else return x;
#
# Example :
#
# Input :
#         A : [1, 4, 10]
#         B : [2, 15, 20]
#         C : [10, 12]
#
# Output : 5
#          With 10 from A, 15 from B and 10 from C.
#


import heapq


class Solution():
    def minimize(self, A, B, C):
        heap = []
        a, b, c = A[0], B[0], C[0]
        arr_names = {"A": A, "B": B, "C": C}
        heap.append((a, 0, "A"))
        heap.append((b, 0, "B"))
        heap.append((c, 0, "C"))
        max_distance = max([abs(a - b), abs(b - c), abs(c - a)])
        min_max_distance = max_distance
        while heap:
            value, index, array = heapq.heappop(heap)
            if array == "A":
                a = A[index]
            elif array == "B":
                b = B[index]
            else:
                c = C[index]
            max_distance = max([abs(a - b), abs(b - c), abs(c - a)])
            if max_distance < min_max_distance:
                min_max_distance = max_distance
            if index < len(arr_names[array]) - 1:
                index += 1
                heapq.heappush(heap, (arr_names[array][index], index, array))
        return min_max_distance

A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]
s = Solution()
print(s.minimize(A, B, C))


# Below is the solution from the site which is less optimized, find why..
#
#     NOTE : This is user generated solution and not an editorial solution
#
# class Solution:
#     # @param A : tuple of integers
#     # @param B : tuple of integers
#     # @param C : tuple of integers
#     # @return an integer
#     def minimize(self, A, B, C):
#         i = 0
#         j = 0
#         k = 0
#         l = len(A)
#         m = len(B)
#         n = len(C)
#         ret = 2**31-1
#         while i < l and j < m and k < n:
#             tempMin = min(A[i],B[j],C[k])
#             tempMax = max(A[i],B[j],C[k])
#             ret = min(ret, tempMax-tempMin)
#             if ret == 0:
#                 return ret
#             if tempMin == A[i]:
#                 i += 1
#             elif tempMin == B[j]:
#                 j += 1
#             else:
#                 k += 1
#         return ret
#
