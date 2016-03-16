# -*- coding: utf-8 -*-

from binheap import BinaryHeap


class PriorityQItem(object):
    """Represents an item in a priority queue.

    Contains some value and a priority integer.
    A higher interger is a higher priority.

    """
    def __init__(self, val, priority=1):
        """Constructor function of a Priority Queue Item."""
        self._val = val
        self._priority = priority

    def __lt__(self, other_item):
        """Checking if self is less than other item based on priority."""
        return self._priority < other_item._priority

    def __gt__(self, other_item):
        """Checking if self is greater than other item based on priority."""
        return self._priority > other_item._priority


class PriorityQ(object):
    """Python implementation of the Priority Queue data structure."""

    def __init__(self, iter=None):
        """Constructor function of a Priority Queue."""
        self._priority_heap = BinaryHeap()

        if iter:
            for val in iter:
                if isinstance(val, PriorityQItem):
                    self.insert(val)
                else:
                    self.insert(PriorityQItem(val))

    def insert(self, item):
        """Insert a new item into our queue."""
        self._priority_heap.push(item)

    def pop(self):
        """Remove the most important item from the queue."""
        popped_val = self._priority_heap._heap_list[0]
        self._priority_heap.pop()
        return popped_val

    def peek(self):
        """Return the most important item without removing it from the heap."""
        return self._priority_heap._heap_list[0]