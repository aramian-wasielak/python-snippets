class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_iterate_dfs(root):
    if root is None:
        return 0

    depth = 0
    stack = [(root, 1)]
    while len(stack) > 0:
        node, cur_depth = stack.pop()
        if node is not None:
            depth = max(depth, cur_depth)
            stack.append([node.left, cur_depth + 1])
            stack.append([node.right, cur_depth + 1])

    return depth


def iterate_bfs():
    pass


def main():
    print('hello world222')


if __name__ == 'main':
    main()
