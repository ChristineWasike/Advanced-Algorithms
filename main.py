# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from mergeSort import mergesort
from mergeArrays import merge_arrays


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [2, 8, 5, 3, 9, 4, 1, 7]
    # print(mergesort(arr))
    arr1 = [-1, -3, 5, 7, 9]
    arr2 = [10, 8, 6, 4, 2]

    arr8 = set()
    i = 0
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[i] > arr2[i]:
            arr8.add(arr2[i])
            arr2.remove(arr2[i])
        else:
            arr8.add(arr1[i])
            arr1.remove(arr1[i])

    print(list(arr8))

    # print(merge_arrays(arr1, arr2))

    # print(-1 > 10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
