def singlenum(nums):
    unique = 0
    for i in nums:
        unique ^= i
    return unique

if __name__ == "__main__":
    print(singlenum([2,2,1]))