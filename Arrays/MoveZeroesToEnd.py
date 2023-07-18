def moveZeros(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(0)
            nums.remove(0)
    return nums

if __name__ == "__main__":
    print(moveZeros([0,1,0,3,12]))