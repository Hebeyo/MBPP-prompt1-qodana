def common_in_nested_lists(nestedlist):
    n = len(nestedlist)
    if n == 0:
        return []
    common = nestedlist[0]
    for i in range(1, n):
        common = set(common) & set(nestedlist[i])
    return list(common)
