# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, current_path, paths):
            if not node:
                return

            # Append the current node's value to the current path
            current_path += str(node.val)
            print(node.val)
            
            # If it's a leaf node (no left or right children), store the path
            if not node.left and not node.right:
                paths.append(current_path)
            else:
                # Otherwise, continue DFS for both children with '->' added to the path
                current_path += '->'
                dfs(node.left, current_path, paths)
                dfs(node.right, current_path, paths)
           
        # Edge case: if root is None, return an empty list
        if not root:
            return []

        paths = []
        dfs(root, "", paths)
        return paths
