def findMaxConsecutiveOnes(nums):
    maxi=0
    count=0
    for i in range(len(nums)):
        if nums[i] == 1:
            count+=1
        else:
            count=0
        if count>maxi:
            maxi=count
    return maxi


if __name__ == "__main__":
     print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
                
                
                
            
            
        