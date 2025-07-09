from src.min_heap import MinHeap

def kth_largest(nums: list[int], k: int) -> int:
    """Возвращает k-й по величине элемент (1-indexed)"""
    heap = MinHeap()
    for x in nums:
        heap.push(x)
        if len(heap) > k:
            heap.pop()
    return heap.peek()

