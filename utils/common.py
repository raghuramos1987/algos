def swap(arr, i, j):
    if i != j:
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
