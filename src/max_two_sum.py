import sys
from typing import List, Final

def max_two_sum(nums: List[int]) -> int:
    """Сумма двух наибольших различных элементов (O(n), O(1))."""
    MIN_INT: Final[int] = -sys.maxsize - 1
    max1: int = MIN_INT
    max2: int = MIN_INT

    for x in nums:
        if x > max1:
            max1, max2 = x, max1
        elif max2 < x != max1:
            max2 = x
            
    return max1 + max2