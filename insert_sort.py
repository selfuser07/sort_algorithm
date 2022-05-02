def insert_sort(arr):
    """Insert sorting algorithm"""
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
