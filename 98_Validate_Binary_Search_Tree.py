# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        self.LDR(root, res)
        if sorted(list(set(res))) == res:
            return True
        else:
            return False
    def LDR(self, root: TreeNode, inputlist: list):
        if root:
            self.LDR(root.left, inputlist)
            inputlist.append(root.val)
            self.LDR(root.right, inputlist)
