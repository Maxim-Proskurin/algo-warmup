from src.min_heap import MinHeap

def kth_largest(nums: list[int], k: int) -> int:
    """Возвращает k-й по величине элемент массива.

    Алгоритм: поддерживает мин-кучу размера k, поэтому
    время O(n log k), память O(k).

    Args:
        nums: Список целых чисел (len ≥ k).
        k: Позиция (1 = самый большой).

    Returns:
        k-й по величине элемент.

    Examples:
        >>> kth_largest([5, 1, 9, 6], 2)
        6

    """
    heap = MinHeap()
    for x in nums:
        heap.push(x)
        if len(heap) > k:
            heap.pop()
            
    return heap.peek()

