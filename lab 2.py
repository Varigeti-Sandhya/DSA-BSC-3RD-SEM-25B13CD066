# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = 1
        for j in range(i + 1, n):
            if arr[j] < arr [min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
data = [64, 25, 12, 22, 11]
print("Before sorting:", data)
result = selection_sort(data)
print("After sorting: ", result)
