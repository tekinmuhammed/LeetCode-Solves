# 1290. Convert Binary Number in a Linked List to Integer

**Difficulty:** Easy  
**Link:** [LeetCode 1290](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer)

---

## Problem Description

You are given the `head` of a singly linked list where each node contains a binary digit `0` or `1`.  
The linked list represents a binary number, with the **most significant bit at the head**.

Return the **decimal (base-10) value** of the binary number.

---

## Example

### Input
```python
Linked List: 1 -> 0 -> 1
```

### Output
`5`

### Explanation
Binary 101 is equal to 5 in decimal.

---

## Constraints

- The linked list will not be empty.
- The linked list contains between 1 and 30 nodes.
- Each node's value is either `0` or `1`.

---

## Approach & Explanation

The binary number is stored in the linked list with the **most significant bit first**, so we can:

- Initialize an accumulator (`num`) as 0.
- Traverse the linked list:
  - For each node, shift the current number left by 1 (equivalent to multiplying by 2).
  - Add the current bit (`node.val`) to the number.
- Continue until the end of the list.

This method simulates binary-to-decimal conversion in linear time.

---

### Time and Space Complexity**

- **Time Complexity:** `O(n)` – We traverse the linked list once.

- **Space Complexity:** `O(1)` – No extra space is used besides a few variables.

### Tags

`Linked-List`, `Math`, `Binary`, `Bit-Manipulation`

### Summary
This is a clean and efficient implementation of binary to decimal conversion using a singly linked list.
No extra list or string conversion is needed – we just simulate left-shifting and accumulation. 