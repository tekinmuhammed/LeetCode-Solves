# 1290. Convert Binary Number in a Linked List to Integer

# **Difficulty:** Easy  
# **Link:** [LeetCode 1290](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer)

# 🧠 Problem Description 
# [Github LeetCode 1290. Convert Binary Number in a Linked List to Integer](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1290.%20Convert%20Binary%20Number%20in%20a%20Linked%20List%20to%20Integer)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        num = 0
        while head:
            num = num * 2 + head.val
            head = head.next
        return num