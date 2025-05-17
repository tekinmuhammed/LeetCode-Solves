# LeetCode 3318 - Find X-Sum of All K-Long Subarrays I

## 🔗 Problem Link
[LeetCode 3318 - Find X-Sum of All K-Long Subarrays I](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/)

## 🧠 Problem Description 

Given an array `nums`, an integer `k` (length of subarrays), and an integer `x`, the task is to compute the **X-Sum** for every subarray of length `k`. The X-Sum is defined as the sum of the `x` most frequent elements in the subarray, where each element is multiplied by its frequency.

If multiple elements have the same frequency, prefer the one with the higher value.

## 🧪 Example

```python
Input: nums = [1, 2, 2, 3, 3, 3], k = 3, x = 2
Output: [6, 10, 13, 15]
```

## 💡 Approach
For every sliding window of size `k`:

Count the frequency of elements using `collections.Counter`.

Sort elements first by frequency (descending), then by value (descending).

Select the top `x` most frequent elements.

Multiply each element by its frequency and take the sum.

## 🧮 Complexity
**Time:** O((n - k + 1) * k log k)

**Space:** O(k)

## 📌 Tags
`sliding-window`, `frequency-count`, `sorting`, `array`, `python`