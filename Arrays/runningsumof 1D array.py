def runningSum(nums):
    for i in range(1,len(nums)):
        nums[i]=nums[i]+nums[i-1]
    return nums

if __name__ == "__main__":
    print(runningSum([1,2,3,4]))