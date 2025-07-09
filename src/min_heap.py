class MinHeap:
    def __init__(self) -> None:
        self._data: list[int] = []

    def __len__(self) -> int:
        return len(self._data)

    def peek(self) -> int:
        return self._data[0]

    def push(self, value: int) -> None:
        self._data.append(value)      # вставили в хвост
        i = len(self._data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i] >= self._data[parent]:
                break
            self._data[i], self._data[parent] = self._data[parent], self._data[i]
            i = parent

    def pop(self) -> int:
        if not self._data:
            raise IndexError("pop from empty heap")
        minimum = self._data[0]
        last = self._data.pop()        
        if self._data:
            self._data[0] = last
            i = 0
            size = len(self._data)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i
                if left < size and self._data[left] < self._data[smallest]:
                    smallest = left
                if right < size and self._data[right] < self._data[smallest]:
                    smallest = right
                if smallest == i:
                    break
                self._data[i], self._data[smallest] = (
                    self._data[smallest],
                    self._data[i],
                )
                i = smallest
        return minimum
