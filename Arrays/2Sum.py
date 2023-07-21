def twosum(nums,target):
    n = len(nums)
    M = {}
    for i in range(n):
        x = target - nums[i]
        if nums[i] in M:
            return [M[nums[i]],i]
        else:
            M[x] = i

if __name__ == "__main__":
    print(twosum([2,7,1,5],9))