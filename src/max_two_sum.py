import sys
from typing import List

def max_two_sum(nums: List[int]) -> int:
    min_int = -sys.maxsize - 1
    max1 = max2 = min_int       

    for x in nums:
        if x > max1:
            max1, max2 = x, max1
        elif x > max2 and x != max1:
            max2 = x

    return max1 + max2
