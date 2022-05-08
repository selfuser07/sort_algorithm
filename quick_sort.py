def quick_sort(arr):
	"""Quick sorting alogorithm"""
	if len(arr) < 2:
		return arr
	middle = arr[0]
	less = [i for i in arr[1:] if i < middle]
	greater = [i for i in arr[1:] if i > middle]
	eq = [i for i in arr if i == middle]
	return quick_sort(less) + eq + quick_sort(greater)
	

