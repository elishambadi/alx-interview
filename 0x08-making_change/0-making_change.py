#!/usr/bin/python3
"""Making Change"""

def makeChange(coins: list, total: int) -> int:
    """
        Making Change function
    """
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Base case: 0 coins needed to make 0 total

    # Compute the minimum coins needed for all values from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                res = min(min_coins[amount], min_coins[amount - coin] + 1)
                min_coins[amount] = res

    # If the total cannot be met by any number of coins, return -1
    return min_coins[total] if min_coins[total] != float('inf') else -1
