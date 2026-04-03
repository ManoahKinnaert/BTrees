from BTrees.core.node import Node

class BTree:
    def __init__(self, root: Node=None):
        self._root: Node = root

    def insert(self, node: Node):
        if self._root is None: self._root = node
        else:
            current = self._root
            spot_found = False
            while not spot_found:
                if node.get_value() < current.get_value():
                    if current.get_left() is None:
                        spot_found = True
                        self._root.set_left(node)
                    else: current = current.get_left()
                else:
                    if current.get_right() is None:
                        spot_found = True
                        self._root.set_right(node)
                    else: current = current.get_right()

    def remove(self, node: Node):
        pass