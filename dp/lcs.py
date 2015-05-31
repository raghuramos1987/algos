def lcs(a1, a2, my_map=None):
    if my_map is None:
        my_map = {}
    i, j = len(a1), len(a2)
    if i > 0 and j > 0:
        if (i,j) in my_map:
            return my_map[(i,j)]
        if a1[-1] == a2[-1]:
            my_map[(i,j)] = lcs(a1[:-1], a2[:-1]) + 1
        else:
            my_map[(i,j)] = max(lcs(a1[:-1], a2), lcs(a1, a2[:-1]))
        return my_map[(i,j)]
    else:
        return 0

if __name__ == '__main__':
    print lcs([1,1,2,3,4], [1,1,2,4,5])
    print lcs([11,3,4], [1,1,3,2,4])
