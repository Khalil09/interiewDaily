class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
  # My solution
  result = []
  def solution(root, height, h):
      nonlocal result
      if root == None:
          return
      if h == height:
          result.append(root.value)
          return
      solution(root.left, height, h+1)
      solution(root.right, height, h+1)
  solution(root, height, 1)

  return result

# A more beatiful solution....
# def valuesAtHeight(root, height):
#   if root == None:
#     return []
#   if height == 1:
#     return [root.value]
#
#   leftNodeValues = valuesAtHeight(root.left, height - 1)
#   rightNodeValues = valuesAtHeight(root.right, height - 1)
#
#   return leftNodeValues + rightNodeValues

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
# a.right.left = Node(6)
# a.right.left.left = Node(9)
print(valuesAtHeight(a, 3))
