inf = open('inversions.txt', 'r')
inp = [int(i) for i in inf.xreadlines()]

def merge_sort(inp, l, r):
    if l >= r:
        return [], 0
    if l == (r-1):
        return [inp[l]], 0
    m = (l+r) / 2
    inp1, linv = merge_sort(inp, l, m)
    inp2, rinv = merge_sort(inp, m, r)
    len1 = len(inp1)
    len2 = len(inp2)
    i = 0
    j = 0
    res = []
    outinv = linv + rinv
    while i < len1 or j < len2:
        if i == len1:
            res.extend(inp2[j:])
            break
        elif j == len2:
            res.extend(inp1[i:])
            break
        if inp1[i] < inp2[j]:
            res.append(inp1[i])
            i += 1
        else:
            res.append(inp2[j])
            j += 1
            outinv += (len1-i)
    return res, outinv

print merge_sort(inp, 0, len(inp))[-1]
