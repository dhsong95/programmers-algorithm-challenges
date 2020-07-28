import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, x, y, data):
        node = Node(x, y, data)
        if not self.root:
            self.root = node
            return

        parent = self.root
        while True:
            if node.x < parent.x:
                if parent.left_child:
                    parent = parent.left_child
                else:
                    parent.left_child = node
                    break
            elif node.x > parent.x:
                if parent.right_child:
                    parent = parent.right_child
                else:
                    parent.right_child = node
                    break

    def _preorder_traversal(self, node, visited):
        if node.data in visited:
            return

        visited.append(node.data)
        if node.left_child:
            self._preorder_traversal(node.left_child, visited)
        if node.right_child:
            self._preorder_traversal(node.right_child, visited)

    def _postorder_traversal(self, node, visited):
        if node.data in visited:
            return

        if node.left_child:
            self._postorder_traversal(node.left_child, visited)
        if node.right_child:
            self._postorder_traversal(node.right_child, visited)
        visited.append(node.data)

    def preorder_traversal(self):
        visited = list()
        self._preorder_traversal(self.root, visited)
        return visited

    def postorder_traversal(self):
        visited = list()
        self._postorder_traversal(self.root, visited)
        return visited


def solution(nodeinfo):
    tree = Tree()
    nodes = list()
    for idx, (x, y) in enumerate(nodeinfo):
        nodes.append((-y, x, idx+1))

    nodes = sorted(nodes)
    for y, x, data in nodes:
        y = -y
        tree.insert(x, y, data)

    preorder = tree.preorder_traversal()
    postorder = tree.postorder_traversal()

    return [preorder, postorder]


if __name__ == "__main__":
    nodeinfo = [
        [5, 3], [11, 5], [13, 3], [3, 5],
        [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]
    ]
    result = [
        [7, 4, 6, 9, 1, 8, 5, 2, 3],
        [9, 6, 5, 8, 1, 4, 3, 2, 7]
    ]
    assert solution(nodeinfo) == result
