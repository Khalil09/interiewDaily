class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

  def __str__(self):
    # preorder traversal
    answer = str(self.key)
    if self.left:
      answer += str(self.left)
    if self.right:
      answer += str(self.right)
    return answer

larger_bst = (0, None)

def largest_bst_subtree(root):
    global larger_bst
    if root is None:
        return 0, True, (float("-inf"), float("inf"))
    else:
        size_left, is_bst_l, min_max_l = largest_bst_subtree(root.left)
        size_right, is_bst_r, min_max_r = largest_bst_subtree(root.right)
        if not is_bst_l and is_bst_r:
            return (size_left + size_right + 1), False, (float("-inf"), float("inf"))
        else:
            if root.key > min_max_l[0] and root.key < min_max_r[1]:
                if (size_left + size_right + 1) > larger_bst[0]:
                    larger_bst = ((size_left + size_right + 1), root)
                return (size_left + size_right + 1), True, (max(root.key, min_max_l[0]), min(root.key, min_max_r[1]))
            else:
                return (size_left + size_right + 1), False, (float("inf"), float("-inf"))


#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
node.right.left.left = TreeNode(3)
largest_bst_subtree(node)
print(larger_bst[1])
#749
