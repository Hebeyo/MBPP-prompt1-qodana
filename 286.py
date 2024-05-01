def max_sub_array_sum_repeated(arr, n, k):
    if k == 1:
        max_so_far = -2147483648
        max_ending_here = 0
        for i in range(n):
            max_ending_here = max_ending_here + arr[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far
    else:
        max_so_far = -2147483648
        max_ending_here = 0
        for i in range(n * k):
            max_ending_here = max_ending_here + arr[i % n]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far
