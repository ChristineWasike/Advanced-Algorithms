# You are given two sorted arrays that both only contain integers.
# Your task is to find a way to merge them into a single one, sorted in asc order.
# Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

# You don't need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers.
# If both arr1 and arr2 are empty, then just return an empty array.

# Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2 may have same integers.
# Remove duplicated in the returned result.

def merge_arrays(arr1, arr2):
    if len(arr1) == 0 and len(arr2) == 0:
        return arr1 or arr2

    arr3 = set()
    i = 0
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[i] > arr2[i]:
            arr3.add(arr2[i])
            arr2.remove(arr2[i])
        else:
            arr3.add(arr1[i])
            arr1.remove(arr1[i])

    while len(arr1) != 0:
        arr3.add(arr1[i])
        arr1.remove(arr1[i])

    while len(arr2) != 0:
        arr3.add(arr2[i])
        arr2.remove(arr2[i])

    return list(arr3)
