# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        nodeSet = set()
        while head:
            if head in nodeSet:
                return True
            nodeSet.add(head)
            head = head.next
        return False
    
'''
https://leetcode.com/problems/linked-list-cycle/
------------------------------------------------

'''