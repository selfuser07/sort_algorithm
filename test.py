from bubble_sort import bubble_sort
from choose_sort import choose_sort
from insert_sort import insert_sort


def test_case(fun, index, arr):
    print("Test case #", index, ": ", end="")
    arr_sorted = arr.copy()
    arr_sorted.sort()
    print("OK" if fun(arr) == arr_sorted else "FAIL")


def test_algorithm(algorithm):
    print(algorithm.__doc__)
    index = 1
    for arr in ([2, 1], [5, 8, 9, 10, 1, 0, -1], [-4, -6, -100, 0, 90], [], [1],
                ['w', 'a', 'b', 'd', 'r', 'e', 'f'], ["dsds", "aassa", "123", ""]):
        test_case(algorithm, index, arr)
        index += 1


if __name__ == "__main__":
    for f in bubble_sort, insert_sort, choose_sort:
        test_algorithm(f)
