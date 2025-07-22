# 1948. Delete Duplicate Folders in System

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1948](https://leetcode.com/problems/delete-duplicate-folders-in-system/)

---

## Problem Description

You are given a list of folder paths in a file system. Each path is a list of strings representing the folder names in the path. Two folders are considered **duplicate** if they have the **same structure and subfolder names**, regardless of their parent folders.

You need to **delete all duplicate folders** and return the remaining folders as a list of paths.

### Example

**Input:**
```python
paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["c","b","x"]]
```

### Output:
```python
[["a"],["c"]]
```

### Approach

This problem requires detecting and removing duplicate folder **structures**, not just by name. The approach involves:

1. **Building a Trie Tree** of all folders, where each node represents a folder name.

2. **Serializing Subtrees:** For each node, we perform a post-order DFS traversal to generate a unique string representation of its entire subtree (e.g., `"b(x)"`).

3. **Detecting Duplicates:** We use a hash map (`Counter`) to record the frequency of each serialized subtree. If a serialization occurs more than once, it is considered a duplicate.

4. **Pruning the Tree:** In a second DFS traversal, we skip nodes whose subtree serialization appears more than once.

5. **Collecting Valid Paths:** During traversal, we collect valid (non-deleted) folder paths.

### Complexity

- **Time Complexity:** `O(N log N)`, where `N` is the total number of folder nodes (due to sorting child serials).

- **Space Complexity:** `O(N)`, for the Trie and the hash map storing serializations.

### Tags
`Trie`, `DFS`, `HashMap`, `Serialization`, `Tree-Pruning`

### Key Insights

- Tree serialization helps detect structural duplicates.

- Sorting child nodes before serialization ensures consistent representation, regardless of insertion order.

- Two-pass DFS (construct & operate) is a common technique in tree cleanup problems.