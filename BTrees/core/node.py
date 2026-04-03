class Node:
    def __init__(self, value, left=None, right=None, is_root=False):
        self._value = value
        self._left = left
        self._right = right
        self._is_root = is_root

    def is_root(self): return self._is_root

    def get_value(self): return self._value

    def get_left(self): return self._left

    def get_right(self): return self._right
