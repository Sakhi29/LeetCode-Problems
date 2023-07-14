def maximumWealth(accounts):
    maxWealth=0
    for i in range(len(accounts)):
        totalWealth = sum(accounts[i])
        maxWealth = max(maxWealth, totalWealth)
    return maxWealth

if __name__ == "__main__":
    print(maximumWealth([[1,5],[7,3],[3,5]]))