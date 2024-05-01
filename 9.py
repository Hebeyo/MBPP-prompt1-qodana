def find_Rotations(s):
    n = len(s)
    for i in range(1,n+1):
        if s == s[i:] + s[:i]:
            return i
    return n
