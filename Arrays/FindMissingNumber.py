def missingNumber(nums):
    l=len(nums)
    nums.sort()
    c=0

    for i in nums:
        if i!=c:
            return c
        c+=1
    else:
        return c
    
if __name__ == "__main__":
    print(missingNumber([3,0,1]))