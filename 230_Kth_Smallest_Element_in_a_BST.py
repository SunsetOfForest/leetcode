# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    count = 0
    returnVal = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorderTraversal(root, k)
        Solution.count = 0
        return Solution.returnVal

    def inorderTraversal(self, root: TreeNode, k:int) -> int:
        if root:
            self.inorderTraversal(root.left, k)
            Solution.count += 1
            if Solution.count == k:
                Solution.returnVal = root.val
            self.inorderTraversal(root.right, k)
