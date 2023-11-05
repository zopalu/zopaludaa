class ItemValue:

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val / wt  # Use floating-point division for fractions

    def __lt__(self, other):
        return self.cost > other.cost  # Sort in non-increasing order

def fractionalKnapSack(wt, val, capacity):
    """Function to get the maximum value"""
    n = len(wt)
    iVal = [ItemValue(wt[i], val[i], i) for i in range(n)]

    # Sorting items by cost in non-increasing order
    iVal.sort()

    totalValue = 0
    for i in iVal:
        curWt = i.wt
        curVal = i.val
        if capacity - curWt >= 0:
            capacity -= curWt
            totalValue += curVal
        else:
            fraction = capacity / curWt
            totalValue += curVal * fraction
            break
    return totalValue

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    wt = []
    val = []

    print("Enter the weights:")
    for i in range(n):
        w = int(input())
        wt.append(w)

    print("Enter the Profits:")
    for i in range(n):
        v = int(input())
        val.append(v)

    capacity = int(input("Enter the capacity of the knapsack: "))

    maxValue = fractionalKnapSack(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)
