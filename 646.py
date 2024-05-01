def No_of_cubes(N,K):
    No = 0
    for i in range(N-K+1):
        for j in range(N-K+1):
            for k in range(N-K+1):
                No += 1
    return No
