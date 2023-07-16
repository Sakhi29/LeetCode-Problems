def checkIfExist(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if i!=j and ((arr[i] == arr[j]+arr[j]) or (arr[i]+arr[i] == arr[j])):
                return True
    else:
        return False
    
if __name__ == "__main__":
    print(checkIfExist([10,2,5,3]))