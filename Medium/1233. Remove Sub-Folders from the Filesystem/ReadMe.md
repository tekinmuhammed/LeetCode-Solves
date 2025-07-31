# 🗂️ LeetCode 1233 - Remove Sub-Folders from the Filesystem

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1233](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem)

---

## 🧩 Problem Description

Given a list of folder paths, remove all sub-folders so that only top-level folders remain.  
A sub-folder is defined as a folder that appears under another folder path.

You are given a list of strings `folder` representing paths. Return a list of strings representing the folders after removing all sub-folders.

---

## 💡 Example

### Input:
```python
folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
```

## Output:
```python
['/a', '/c/d', '/c/f']
```

## 🚀 Approach

- Sort the folder paths lexicographically so that parent folders appear before their subfolders.

- Iterate through the sorted list, and check if the current folder starts with the `previous` top-level folder followed by a `/`.

- If it doesn’t, add it to the result and update the `previous` reference.

This ensures that only top-level folders are included.

## 📝 Output

['/a', '/c/d', '/c/f']

## ⏱️ Complexity

- **Time Complexity:** `O(n log n)` – due to sorting

- **Space Complexity:** `O(n)` – for the result list

## 🏷️ Tags

`string`, `sorting`, `greedy`, `filesystem`, `prefix-check`, `leetcode-medium`, `python`

## 📌 Notes

- Sorting ensures parent directories appear before children.

- The trick with `startswith(previous)` combined with `+ "/"` ensures subfolders aren’t mistakenly included.

