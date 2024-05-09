#!/usr/bin/python3
"""
method to determine the number of occurance of a letter
"""
"""
it returns an integer if n is impossible returns 0
"""


def minOperations(n):
    at_movement = 1
    initial_value = 0
    counting = 0
    while at_movement < n:
        if((n - at_movement) % at_movement == 0):
            initial_value = at_movement
            at_movement += initial_value
            counting += 2
        else:
<<<<<<< HEAD
            at_movement += initial_value
            counting += 1
    return counting
=======
            now += start
            counter += 1
    return counter
