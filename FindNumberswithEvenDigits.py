def findNumbers(nums):
    cnt=0
    for i in range(len(nums)):
        if len(str(nums[i]))%2==0:
            cnt+=1
    return cnt
                
if __name__ == "__main__":
    print(findNumbers([12,345,2,6,7896]))