# Counting Sort
def	counting_sort(arr):
    biggest	=	max(arr)
    count = [0] * (biggest + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
data = [4, 2, 2, 8, 3, 3, 1]
print("Before sorting:", data)
result = counting_sort(data)
print("After sorting: ", result)
