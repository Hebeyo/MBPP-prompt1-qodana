def get_max_sum(n):
    res = [0, 1]
    i = 2
    while i < n + 1:
        res.append(max(i, res[int(i / 2)] + res[int(i / 3)] + res[int(i / 4)] + res[int(i / 5)]))
        i += 1
    return res[n]
