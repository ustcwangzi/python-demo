"""
 自定义对象支持迭代
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    # 迭代
    def __iter__(self):
        return iter(self._children)

    # 深度遍历
    def depth_trave(self):
        yield self
        for c in self:
            yield from c.depth_trave()


def run():
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_trave():
        print(ch)


if __name__ == '__main__':
    run()
