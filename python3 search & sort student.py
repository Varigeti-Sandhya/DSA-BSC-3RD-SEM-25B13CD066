import random
import time

def linear_search(a, x):
    # Scan from left to right
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def binary_search(a, x):
    # Works only on a sorted list
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def interpolation_search(a, x):
    # Works on a sorted list
    low = 0
    high = len(a) - 1

    while low <= high and a[low] <= x <= a[high]:

        # If both end values are equal
        if a[low] == a[high]:
            if a[low] == x:
                return low
            return -1

        # Estimate the position
        pos = low + ((x - a[low]) * (high - low)) // (a[high] - a[low])

        if a[pos] == x:
            return pos
        elif a[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1


def bubble_sort(a):
    # Return sorted copy
    arr = list(a)

    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def selection_sort(a):
    # Return sorted copy
    arr = list(a)

    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def insertion_sort(a):
    # Return sorted copy
    arr = list(a)

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(a):
    # Recursive split and merge
    if len(a) <= 1:
        return list(a)

    mid = len(a) // 2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(a):
    # Partition recursively; return sorted copy
    arr = list(a)

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def check_sort(name, fn, data):
    t = time.perf_counter()
    out = fn(data)
    ms = (time.perf_counter() - t) * 1000
    return name, ms, out == sorted(data)


def main():
    random.seed(7)
    n = 150

    base = [random.randrange(40) for _ in range(n)]

    cases = {
        'random': base,
        'sorted': sorted(base),
        'reverse': sorted(base, reverse=True),
        'duplicate-heavy': [i % 5 for i in range(n)]
    }

    algs = [
        ('bubble', bubble_sort),
        ('selection', selection_sort),
        ('insertion', insertion_sort),
        ('merge', merge_sort),
        ('quick', quick_sort)
    ]

    print(f"{'case':16}{'algorithm':12}{'ms':>10}  status")

    for case, data in cases.items():
        for name, fn in algs:
            _, ms, ok = check_sort(name, fn, data)
            print(
                f"{case:16}{name:12}{ms:10.3f}  "
                f"{'OK' if ok else '! WRONG'}"
            )

    s = sorted(base)
    target = s[len(s) // 2]

    print(
        'Search indices:',
        linear_search(s, target),
        binary_search(s, target),
        interpolation_search(s, target)
    )


if __name__ == '__main__':
    main()