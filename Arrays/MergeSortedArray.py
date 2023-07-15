def merge(nums1,nums2,m,n):
    for j in range(n):
        nums1[m+j] = nums2[j]
    nums1.sort()
    return nums1

if __name__ == "__main__":
    print(merge([1,2,3,0,0,0],[2,5,6],3,3))
