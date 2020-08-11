class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def count_unival_subtrees(root):
    global count_unival
    if root is None:
        return None
    else:
        left = count_unival_subtrees(root.left)
        right = count_unival_subtrees(root.right)
        if left == None and right == None:
            count_unival += 1
        elif (left == None or right == None) and (root.val == left or root.val == right):

           count_unival += 1
        elif root.val == left  and root.val == right:
           count_unival += 1

    return root.val

count_unival = 0
a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)
a.right.left.right.right = Node(1)

 #   0
 #  / \
 # 1   0
 #    / \
 #   1   0
 #  / \
 # 1   1
#       \
#        1

count_unival_subtrees(a)
print(count_unival)
# 5
