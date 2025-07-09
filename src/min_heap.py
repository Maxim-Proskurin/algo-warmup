class MinHeap:
    """Простейшая бинарная куча для целых чисел.

    Поддерживает операции push, pop, peek за O(log n).
    """

    def __init__(self) -> None:
        """Создание пустой кучи."""
        self._data: list[int] = []

    def __len__(self) -> int:
        """Возвращает кол-во элементов."""
        return len(self._data)

    def peek(self) -> int:
        """Возвращает минимальный элемент, не удаляя его."""
        return self._data[0]

    def push(self, value: int) -> None:
        """Добавляет элемент в кучу.
        
        Args:
            value: Новое целое число, которое нужно вставить.
            
        Examples:
            >>> h = MinHeap()
            >>> h.push(4)
            >>> h.push(2)
            >>> len(h)
            2

        """
        self._data.append(value)      
        i = len(self._data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i] >= self._data[parent]:
                break
            self._data[i], self._data[parent] = self._data[parent], self._data[i]
            i = parent

    def pop(self) -> int:
        """Удаляет и возвращает минимальный элемент.
        
        Raises:
            IndexError: Если куча пуста.
        
        Examples:
            >>> h = MinHeap()
            >>> h.push(3); h.push(1)
            >>> h.pop()
            1

        """
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