from src.max_two_sum import max_two_sum


def test_examples() -> None:
    assert max_two_sum([5, 1, 9, 6]) == 15
    assert max_two_sum([1, 1, 2, 3]) == 5
