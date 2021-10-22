def merge(arr1, arr2):
    arr3 = []
    i = 0
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[i] > arr2[i]:
            arr3.append(arr2[i])
            arr2.remove(arr2[i])
        else:
            arr3.append(arr1[i])
            arr1.remove(arr1[i])

    while len(arr1) != 0:
        arr3.append(arr1[i])
        arr1.remove(arr1[i])

    while len(arr2) != 0:
        arr3.append(arr2[i])
        arr2.remove(arr2[i])

    return arr3


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2
    arr1 = arr[:midpoint]
    arr2 = arr[midpoint:]

    arr1 = mergesort(arr1)
    arr2 = mergesort(arr2)

    return merge(arr1, arr2)
