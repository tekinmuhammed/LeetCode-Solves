# 61. Rotate List 

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 61](https://leetcode.com/problems/rotate-list/description/)

# 🧠 Problem Description
# [Github LeetCode 61. Rotate List ](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/61.%20Rotate%20List) 

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # 1. length bul
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # 2. k mod length
        k = k % length
        if k == 0:
            return head
        
        # 3. circular yap
        tail.next = head
        
        # 4. yeni tail bul (length - k - 1 adım)
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
        
        # 5. yeni head ve koparma
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head