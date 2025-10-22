# 🔢 3349. Adjacent Increasing Subarrays Detection I

# **Difficulty:** Easy
# **Link:** [LeetCode 3349](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/)

# 🧠 Problem Description
# [Github LeetCode 3349. Adjacent Increasing Subarrays Detection I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3349.%20Adjacent%20Increasing%20Subarrays%20Detection%20I)

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