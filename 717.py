def sd_calc(data):
    n = len(data)
    if n <= 1:
        return 0.0
    mean, sd = sum(data)/n, 0.0
    for el in data:
        sd += (el - mean)**2
    sd = (sd / (n-1))**0.5
    return sd
