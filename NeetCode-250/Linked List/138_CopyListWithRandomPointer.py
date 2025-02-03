from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        old = head
        while old:
            oldToCopy[old] = Node(old.val)
            old = old.next

        old = head
        while old:
            new = oldToCopy[old]
            new.next = oldToCopy[old.next]
            new.random = oldToCopy[old.random]
            old = old.next
        return oldToCopy[head]