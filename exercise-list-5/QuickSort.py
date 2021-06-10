# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:32:40 2021
https://stackabuse.com/sorting-algorithms-in-python#quicksort
@author: Stack Abuse
"""

import random

# There are different ways to do a Quick Sort partition, this implements the
# Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

"""
Here, the algorithm starts to differ from the original code on Stack Abuse.
"""
import timeit, random
from numpy import array

# List of random arrays. Each array contains 500 random
# number, sampled without replacement.
randomlist_list = []
for i in range(0,100):
    random_list = random.sample(range(0,5000),500)
    randomlist_list.append(random_list)

class QuickSortAlgorithmTest(object):
    """docstring for """

    def __init__(self,random_list):
        self.random_list=random_list
    
    def test(self):
        t = timeit.Timer('quick_sort(randomlist_list[0])', globals=globals())
        a = t.repeat(repeat=100,number=1)        
        return array(a).mean()

QuickSortAlgorithmTest(randomlist_list[0]).test()