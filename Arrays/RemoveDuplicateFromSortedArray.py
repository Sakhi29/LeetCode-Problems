def removeDuplicate(nums):
    j = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    return j

if __name__ == "__main__":
    print(removeDuplicate([1,1,2]))
