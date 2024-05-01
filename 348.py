def find_ways(M):
    n = M // 2
    a = 1
    for i in range(0, n):
        a *= (2 * n - i)
        a //= (i + 1)
    b = a // (n + 1)
    return b
