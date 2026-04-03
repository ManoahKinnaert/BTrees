from typing import Any

class Node:
    def __init__(self, value: Any, left: Node=None, right: Node=None, is_root: bool=False):
        self._value: Any = value
        self._left: Node = left
        self._right: Node = right
        self._is_root: bool = is_root

    def is_root(self): return self._is_root

    def get_value(self): return self._value

    def get_left(self): return self._left

    def get_right(self): return self._right

    def set_left(self, node: Node): self._left = node

    def set_right(self, node: Node): self._right = node