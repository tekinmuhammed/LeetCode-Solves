# 🔢 3349. Adjacent Increasing Subarrays Detection I

**Difficulty:** Easy  
**Link:** [LeetCode 3349](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/)

## 💬 Problem Description  
You are given an integer array `nums` and an integer `k`.  
Your task is to determine if there exist **two adjacent subarrays** of length `k` each such that **both are strictly increasing**.  

Return `True` if such subarrays exist, otherwise `False`.

---

## 💡 Intuition  
We slide a window of size `2k` across the array.  
At each step, we split the window into two parts:  
- The **first subarray**: `nums[i - k : i]`  
- The **second subarray**: `nums[i : i + k]`  

We then check whether **both subarrays** are strictly increasing — meaning every element is smaller than the next one.  

If we find any such pair, we can immediately return `True`.  
If we finish iterating without finding one, we return `False`.

---

## 🧠 Example  
```python
Input: nums = [1, 2, 3, 4, 2, 3, 4, 5], k = 3
Output: True
```

### Explanation:

-  First increasing subarray = [1, 2, 3]

- Second increasing subarray = [2, 3, 4]
- - Both are strictly increasing and adjacent → ✅

### 🧰 Code Implementation
```python
class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)

        # i, ikinci alt dizinin başladığı indeksi gösterir (b = i)
        # o yüzden ilk alt dizi a = i - k olur
        for i in range(k, n - k + 1):
            first = nums[i - k:i]
            second = nums[i:i + k]

            # iki alt dizi de strictly increasing mi kontrol et
            if all(first[j] < first[j + 1] for j in range(k - 1)) and \
               all(second[j] < second[j + 1] for j in range(k - 1)):
                return True

        return False
```

### 📊 Complexity Analysis

- **Time Complexity:**	`O(n * k)` — for each possible split, we check up to `2k` elements.

- **Space Complexity:**	`O(k)` — for storing the temporary subarrays.

### 🧷 Tags
`Array` · `Sliding-Window` · `Two-Pointers` · `Simulation`