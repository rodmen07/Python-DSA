# The owner of a construction company has a surplus of rods of arbitrary lengths. A local contractor offers to buy any of the surplus, as long as all the rods have the same exact integer length, referred to as saleLength. The number of sellable rods can be increased by cutting each rod zero or more times, but each cut has a cost denoted by costPerCut. After all cuts have been made, any leftover rods having a length other than saleLength must be discarded for no profit. The owner's total profit for the sale is calculated as:
# totalProfit = totalUniformRods x saleLength x salePrice - totalCuts x costPerCut
# where totalUniformRods is the number of sellable rods, salePrice is the per unit length price that thte contractor agreses to pay, and totalCuts is the total number of times the rods needed to be cut.
# Example:
# lengths = [26, 103, 59]
# costPerCut = 1
# salePrice = 10 per unit length
# Explanation:
# Since costPerCut = 1 is very inexpensive, a large number of cuts can be made to reduce the number of wasted pieces. The optimal rod length for maximizing profit is 6, and the rods are cut as shown:
# After performing totalCuts = (1 +3) +(1 + 16) + (1 +8) = 30 cuts, there are totalUniformRods = 4 + 17 + 9 = 30 pieces of length saleLength = 6 that can be sold at salePrice = 10. This yields a total profit of salePrice x totalUniformRods x saleLength - totalCuts x costPerCut = 10 x 30 x 6 -30 x 1 = 1770.
# The function only needs to return the max_profit.

def max_profit(lengths, costPerCut, salePrice):
    max_length = max(lengths)
    max_profit = 0

    for saleLength in range(1, max_length + 1):
        total_uniform_rods = 0
        total_cuts = 0

        for length in lengths:
            pieces, leftover = divmod(length, saleLength)
            total_uniform_rods += pieces
            total_cuts += max(pieces - 1, 0)

            if leftover > 0:
                total_cuts += 1

        profit = (total_uniform_rods * saleLength * salePrice) - (total_cuts * costPerCut)
        max_profit = max(max_profit, profit)

    return max_profit

print(max_profit([26, 103, 59], 1, 10))  # Output: 1770
