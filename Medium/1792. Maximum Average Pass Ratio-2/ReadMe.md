# 1792. Maximum Average Pass Ratio

**Difficulty:** Medium  
**Link:** [LeetCode 1792](https://leetcode.com/problems/maximum-average-pass-ratio/)

---

## Problem Description
There are `n` classes, each with a certain number of passing students `p` and total students `t`.  
You are given `extraStudents` and need to distribute them among the classes.  

Each time a student is added to a class, both `p` and `t` increase by 1.  
The goal is to maximize the **average pass ratio** across all classes.

---

## Example

### Input:
```python
classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
```

### Output:
```python
0.78333
```

### Explanation:

- Add 1 student to the first class → ratio becomes 2/3.

- Add 1 student to the second class → ratio becomes 4/6.

- Average pass ratio = (2/3 + 4/6 + 2/2) / 3 ≈ 0.78333.

### Constraints

- 1 <= classes.length <= 10^5

- 1 <= p <= t <= 10^5

- 1 <= extraStudents <= 10^5

### Approach
**Key Ideas:**

- Each added student increases the pass ratio by:

gain(p,t)=(p+1)/(t+1)​−p/t=(t-p)/(t+1)t
​
- Use a **max heap** to always assign the next student to the class with the maximum gain.

- After distributing all students, compute the final average ratio.

### Time and Space Complexity

- **Time Complexity:** `O(extraStudents · log n)`

- -  Each student insertion involves a heap push and pop.

- **Space Complexity:** `O(n)`

- - For storing heap of classes.

### Tags

`Greedy`, `Heap-(Priority-Queue)`, `Math`

### Notes

- The greedy choice is optimal because each student should always go to the class where they increase the pass ratio the most.

-  Using a **max heap** ensures we efficiently find this class in O(log n) time.