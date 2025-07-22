# 1233. Remove Sub-Folders from the Filesystem

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1233](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/)

---

## Problem Description

You are given a list of folder paths, where each path is a string that represents a folder in a filesystem (e.g., `"/a"`, `"/a/b"`, etc.). If a folder is a **subfolder** of another folder, it should be removed from the result.

A folder `"/a/b"` is a subfolder of `"/a"` if and only if `"/a"` is a prefix of `"/a/b"` and the next character is `'/'`.

### Example

**Input:**  
```python
folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
```

### Output:
```python
["/a","/c/d","/c/f"]
```

### Approach

To efficiently remove subfolders:

1. **Sort** the list of folders lexicographically. This ensures that parent folders come before their subfolders.

2. Initialize an empty result list `res`.

3. Iterate through each folder `path`:

- - If `res` is empty or `path` is not a subfolder of the last added path (`res[-1]`), then it is a valid top-level folder, and we append it to `res`.

- - A subfolder can be detected by checking if it starts with `res[-1] + '/'`.

This greedy approach ensures only top-level folders are included, and any nested folders are skipped.

### Complexity

- **Time Complexity:** `O(n log n)`
Sorting takes O(n log n), and the iteration through the folder list is O(n).

- **Space Complexity:** `O(n)`
For storing the result list.

### Tags
`Greedy`, `String`, `Sorting`

### Notes

- The key insight is that by sorting the folder list, we guarantee that parent directories always come before their subfolders.

- This allows us to process folders in a single pass and skip all subfolders efficiently.