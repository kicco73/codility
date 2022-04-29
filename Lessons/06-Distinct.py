def solution(A):
	return len(set(A))

print(solution([1, 1, 2, 3]))



class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        depth = max(left_depth, right_depth)
        return 1 + depth

def visibleNodes(root):
    return root.depth()