from collections import defaultdict

def lis(arr, my_map=None):
    if my_map is None:
        my_map = defaultdict(int)
    my_map[0] = 1
    l = len(arr)
    ind = 1
    while ind < l:
        vals = [0]
        for i in range(ind):
            if arr[i] < arr[ind]:
                vals.append(my_map[i])
        my_map[ind] = max(vals) +1
        ind += 1
    return max(my_map.values())

if __name__ == '__main__':
    print lis([10, 22, 9, 33, 21, 50, 41, 60, 80])
    print lis([19,1,2,3,4])
