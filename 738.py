def geometric_sum(n):
  if n == 0:
    return 1
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)
