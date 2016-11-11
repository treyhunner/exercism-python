from collections import deque


class BufferFullException(IndexError):
    """Exception raised when writing to full buffer."""


class BufferEmptyException(IndexError):
    """Exception raised when reading from empty buffer."""


class CircularBuffer(deque):

    """A queue with a maximum size."""

    def __init__(self, size):
        self.size = size
        super().__init__()

    def write(self, item):
        if self.is_full:
            raise BufferFullException
        self.append(item)

    def overwrite(self, item):
        if self.is_full:
            self.popleft()
        self.append(item)

    def read(self):
        if not self:
            raise BufferEmptyException
        return self.popleft()

    @property
    def is_full(self):
        return len(self) >= self.size
