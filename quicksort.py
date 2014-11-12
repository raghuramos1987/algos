def swap(arr, i, j):
    if i != j:
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t

def partition(arr, l, r):
    pivot = l
    i = pivot + 1
    j = i
    while i < r:
        if arr[i] < arr[pivot]:
            swap(arr, i, j)
            j += 1
        i += 1
    swap(arr, pivot, j-1)
    return j-1

def quick(arr, l, r):
    if l >= r-1:
        return
    mid = (r - l) / 2 + l
    if not (r - l) % 2:
        mid -= 1
    m = partition(arr, l, r)
    quick(arr, l, m)
    quick(arr, m+1, r)

if __name__ == '__main__':
    with open("quicksort.txt") as fh:
        arr = [int(x) for x in fh.readlines()]
    l = 0
    r = len(arr)
    quick(arr, l, r)
    print arr
