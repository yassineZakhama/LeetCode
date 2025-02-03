from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        def toTree(i, j):
            if i == j:
                return TreeNode(nums[i])
            if i > j:
                return None

            mid = (i + j) // 2
            return TreeNode(nums[mid], toTree(i, mid - 1), toTree(mid+1, j))

        return toTree(0, len(nums)-1)