def digit_distance_nums(n1, n2):
    n1 = str(n1)
    n2 = str(n2)
    if len(n1) > len(n2):
        n2 = '0'*(len(n1)-len(n2)) + n2
    elif len(n1) < len(n2):
        n1 = '0'*(len(n2)-len(n1)) + n1
    return sum([abs(int(n1[i])-int(n2[i])) for i in range(len(n1))])
