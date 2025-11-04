# 🧮 LeetCode 3318 — Find X-Sum of All K-Long Subarrays I

# 🔗 Problem Link
# [LeetCode 3318 - Find X-Sum of All K-Long Subarrays I](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/)

# 🧠 Problem Description
# [Github LeetCode 3318 — Find X-Sum of All K-Long Subarrays I](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/)

from collections import Counter

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            sub = nums[i:i + k]
            freq = Counter(sub)
            
            # En sık görülen x elemanı bul (frekans ve değer sırasına göre)
            most_common = sorted(freq.items(), key=lambda a: (-a[1], -a[0]))[:x]
            
            # Bu elemanların toplam katkısını hesapla
            s = 0
            for num, count in most_common:
                s += num * count
            ans.append(s)

        return ans