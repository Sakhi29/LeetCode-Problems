def kthLargest(nums,k):
    nums.sort(reverse = True)
    return nums[k-1]

if __name__ == "__main__":
    print(kthLargest([3,2,1,5,6],2))
