def validMountainArray(arr):
    place = arr.index(max(arr))
    if place == 0 or place == len(arr) - 1:
        return False
    else:
        value = True
        i = 0
        while i < place:
            if arr[i] >= arr[i+1]:
                value = False
                break
            else:
                i += 1
        i = place + 1
        if value:
            while  i < len(arr):
                if arr[i-1] <= arr[i]:
                    print(i)
                    return False
                else:
                    i += 1
        else:
            return False
        return True
    
if __name__ == "__main__":
    print(validMountainArray([0,3,2,1]))
                