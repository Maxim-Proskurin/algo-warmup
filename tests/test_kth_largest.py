import pytest
from src.kth_largest import kth_largest

@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([5, 1, 9, 6], 2, 6),  # обычный
        ([3, 7, 4, 9], 1, 9),  # k = 1
        ([8, 2, 5], 3, 2),     # k = len(nums)
    ],
)
def test_kth_largest(nums, k, expected): 
    assert kth_largest(nums, k) == expected  
