from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
              n = q.popleft()
              result += n.val
              if n.left:
                  q.append(n.left)
              if n.right:
                  q.append(n.right)

        return result


def reconstruct(preorder, inorder):
    if not preorder or not inorder:
        return None
    if len(preorder) == len(inorder) == 1:
        return Node(preorder[0])

    root = Node(preorder[0])
    root_index = inorder.index(root.val)
    root.left = reconstruct(preorder[1:1+root_index], inorder[:root_index])
    root.right = reconstruct(preorder[root_index+1:], inorder[root_index+1:])

    return root

# Preorder: (Root, Left, Right)
# Inorder: (Left, Root, Right)

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g
#         \
#          h

# left: pre [b, d, e]  ino [d, b ,e] root_index = 3
#   left: pre [d] ino [d] root_index = 1
#       return d
#   right: pre [e] ino [e] root_index = 1
#       return e

# right: pre [c, f, g] ino [f, c, g] root_index = 3
#   left: pre [f] ino [f] root_index = 1
#       return f
#   right: pre [g] ino [g] root_index = 1
#       return g

# The first node from preorder represents the root of the tree. Find the node
# in the inorder array, all the nodes on the left of this index are from left
# tree and the all from right are from the right tree. All the nodes
# inside the interval [1:1+root_index] are the left nodes in preorder.  

tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g', 'h'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g', 'h'])
print(tree)
# abcdefg
