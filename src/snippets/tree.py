import unittest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestTreeMethods(unittest.TestCase):
    @staticmethod
    def generate_tree(depth):
        root = node = TreeNode(1)
        for i in range(depth - 1):
            node.left = TreeNode(i + 2)
            node = node.left
        return root

    def test_tree_depth_dfs_iterate(self):
        test_depth = 10
        root = self.generate_tree(test_depth)

        depth = 1
        stack = [(root, 1)]
        while len(stack) > 0:
            node, cur_depth = stack.pop()
            if node is not None:
                depth = max(depth, cur_depth)
                stack.append([node.left, cur_depth + 1])
                stack.append([node.right, cur_depth + 1])

        self.assertEqual(test_depth, depth)

    def test_tree_depth_bfs_iterate(self):
        # TODO:
        pass


if __name__ == "__main__":
    unittest.main()
