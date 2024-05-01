def k_smallest_pairs(nums1, nums2, k):
    pairs = []
    for i in nums1:
        for j in nums2:
            pairs.append([i,j])
    pairs.sort(key=lambda x:x[0]+x[1])
    return pairs[:k]
