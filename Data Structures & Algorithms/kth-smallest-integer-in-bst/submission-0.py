class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if len(result) >= k:
                return
            result.append(root.val)
            dfs(root.right)
        dfs(root)
        return result[k-1]