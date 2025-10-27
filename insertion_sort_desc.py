def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

data = [5, 2, 9, 1, 7, 3]
print("Original array:", data)
insertion_sort_desc(data)
print("Sorted array (decreasing):", data)
