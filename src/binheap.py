# -*- coding: utf-8-*-


class BinaryHeap(object):
    """Python implementation of a Binary Heap Data Structure."""

    def __init__(self, iter=None):
        """Constructor function for BinaryHeap."""
        self._heap_list = []

        if iter:
            for val in iter:
                self.push(val)

    @property
    def heap_list(self):
        return self._heap_list

    def push(self, val):
        """Put new value into the heap, maintaining the heap property."""
        self._heap_list.append(val)
        self._heap_check_up(self._parent_index(len(self._heap_list) - 1),
                            len(self._heap_list) - 1)

    def pop(self):
        """Remove the top value in the heap, maintaining the heap property."""
        rtn_val = self._heap_list.pop(0)
        self._heap_check_down(0)
        return rtn_val

    def _heap_check_up(self, parent_index, child_index):
        """Check if value of child is greater or less than parent.

        Does a switch if this is true then does a check_up on the new parent
        and its parent.
        """
        if child_index == 0 or parent_index is None:
            return  # end recursion.
        if self._heap_list[child_index] > self._heap_list[parent_index]:
            # Swtich the location of parent and child if child is greater.
            self._heap_list[parent_index], self._heap_list[child_index] = \
                self._heap_list[child_index], self._heap_list[parent_index]
        # go up one level and check the current parent and its parent.
        self._heap_check_up(self._parent_index(parent_index), parent_index)

    def _heap_check_down(self, parent_index):
        """Check if a parent's children has a greater value than the parent.

        Does a switch if this is true starting from left side and then checks
        down on the new child.
        """
        left, right = self._child_index(parent_index)
        try:
            # Check if left is greater than the parent and greater than right.
            if (self._heap_list[left] > self._heap_list[parent_index] and
               self._heap_list[left] > self._heap_list[right]):
                # Switch left and parent
                self._heap_list[parent_index], self._heap_list[left] = \
                    self._heap_list[left], self._heap_list[parent_index]
                # Check down starting from left.
                self._heap_check_down(left)
            # Check if right is greater than the parent and greater than left.
            elif (self._heap_list[right] > self._heap_list[parent_index] and
                  self._heap_list[right] > self._heap_list[left]):
                # Switch right and parent
                self._heap_list[parent_index], self._heap_list[right] = \
                    self._heap_list[right], self._heap_list[parent_index]
                # Check down starting from right.
                self._heap_check_down(right)
            # parent is greater than both left and right.
            return  # end recursion.
        except IndexError:  # If we try to check a non-existing left or right.
            return  # end recursion.

    def _child_index(self, parent_index):
        """Return a tuple of the parent_index' child indexes (Left, Right)."""
        return (2 * parent_index + 1, 2 * parent_index + 2)

    def _parent_index(self, child_index):
        """Return the index of the child_index's parent."""
        return (child_index - 1) // 2
