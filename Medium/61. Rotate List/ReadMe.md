# 61. Rotate List

**Difficulty:** Medium  
**Problem Link:** [LeetCode 61](https://leetcode.com/problems/rotate-list/description/)

---

## Problem
Given the `head` of a linked list, rotate the list to the right by `k` places.

Example:

Input  
head = [1,2,3,4,5], k = 2  

Output  
[4,5,1,2,3]

Explanation  
Rotate 1 steps to the right: [5,1,2,3,4]  
Rotate 2 steps to the right: [4,5,1,2,3]  

---

# Approach

The problem asks us to shift the linked list to the right by `k` positions. If `k` is greater than or equal to the length of the list, the rotations will wrap around and repeat.

To solve this efficiently, we can transform the linked list into a circular list and then break it at the correct position.

Steps:

1. **Handle Edge Cases:** If the list is empty, has only one node, or `k == 0`, no rotation is needed.
2. **Find the Length:** Traverse the list to find its total `length` and locate the current `tail` node.
3. **Optimize `k`:** Since rotating a list of length `L` by `L` times results in the identical list, we can update `k` using the modulo operation: `k = k % length`. If the new `k` is 0, we can just return the `head`.
4. **Form a Circular List:** Connect the current `tail` to the `head` (`tail.next = head`), forming a continuous loop.
5. **Find the New Tail:** The new tail of our rotated list will be located `length - k` steps from the beginning. We traverse `length - k - 1` steps to land exactly on the new tail node.
6. **Break the Circle:** The new head will be the node right after the new tail. We break the circular link by setting `new_tail.next = None` and return the new head.

---

# Code

```python
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
```

---

# Example Walkthrough

Example:

head = [1, 2, 3, 4, 5]  
k = 2

1. **Find length:**  
   Length = 5, Tail = Node(5)

2. **Update k:**  
   k = 2 % 5 = 2

3. **Form circular list:**  
   Node(5).next = Node(1)  
   List looks like an infinite circle: `1 -> 2 -> 3 -> 4 -> 5 -> 1 -> ...`

4. **Find the new tail:**  
   Steps needed = `length - k` = 5 - 2 = 3  
   We start at `head` (1) and move `3 - 1 = 2` steps forward:  
   Step 1: `1 -> 2`  
   Step 2: `2 -> 3`  
   New tail is **Node(3)**.

5. **Find the new head and break the list:**  
   New head = `Node(3).next` = **Node(4)**  
   Break the loop: `Node(3).next = None`  
   
Final list returned:  
[4, 5, 1, 2, 3]

---

# Complexity Analysis

Time Complexity

O(N)

We traverse the list once to find the length (O(N)), and then partially traverse it again to find the new tail (O(N)). The overall time complexity strictly scales linearly with the number of nodes `N`.

Space Complexity

O(1)

We only use a few extra pointers (`length`, `tail`, `new_tail`, `new_head`), so the memory footprint is constant and does not depend on the input size.