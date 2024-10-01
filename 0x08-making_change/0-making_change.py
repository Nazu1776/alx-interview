#!/usr/bin/python3
"""Module that returns a minimum number of coins needed
to make up a given amount"""


def makeChange(coins, total):
    """Function that calculates the fewest number of coins needed
    Args:
        coins (list): list of int representing denominations of coins available
        total (int): The total amount to be made up
    Returns:
        int: Fewest number of coins needed to meet the total amount
            -1 if the total cannot be met by the available coins """
    
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)  # Sort denominations in descending order

    coins_used = 0
    remaining_total = total

    # Loop through each coin denomination
    for coin in coins:
        # Check if the current coin can be used to make change
        while remaining_total >= coin:
            coins_used += 1
            remaining_total -= coin

    # Check if the total amount has been completely covered by available coins
    if remaining_total == 0:
        return coins_used
    else:
        return -1
