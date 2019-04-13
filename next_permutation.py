# Idea is to take the rightmost element i
# and switch it with the rightmost jone
# wich is less than the first first lets
#, last step is to sort the
# 

def next_permutation(arr):

    for i in range(len(arr) - 1, 1, -1):
        for j in range(i - 1, 0, -1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                arr[j + 1:] = sorted(arr[j + 1:])
                return arr


assert next_permutation([1, 0, 3, 2]) == [1, 2]