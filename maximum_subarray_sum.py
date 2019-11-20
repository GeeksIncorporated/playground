# Subproblem is going to be max(sum(A[:i])) = max( sum(A[:i-1])+A[i], A[i])

def max_subarray(A):
    max_subarray_sum = A[0]
    global_max_subarray_sum = max_subarray_sum
    for i in range(1, len(A)):
        max_subarray_sum = max(max_subarray_sum + A[i], A[i])
        max_so_far = max(max_subarray_sum, global_max_subarray_sum)
    return max_so_far


A = [431, -15, 639, 342, -14, 565, -924, 635, 167, -70]
print max_subarray(A)
