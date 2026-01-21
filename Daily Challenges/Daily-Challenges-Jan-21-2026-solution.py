## 3315. Construct the Minimum Bitwise Array II

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3315](https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/description/)

# 🧠 Problem Description
# [Github LeetCode 3315. Construct the Minimum Bitwise Array II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3315.%20Construct%20the%20Minimum%20Bitwise%20Array%20II)

class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for x in nums:
            if x == 2:
                # 2 sayısı (binary 10) için koşulu sağlayan bir değer yoktur.
                ans.append(-1)
            else:
                # x asal sayı olduğu için tektir (2 hariç).
                # Amacımız x'in sonundaki 1 bloğunun en büyük basamağındaki 1'i 0 yapmaktır.
                
                # 1. Adım: x + 1 ile son 1 bloğunu sıfırla ve bir solundaki 0'ı 1 yap.
                # Örn: x = 23 (10111) -> x + 1 = 24 (11000)
                next_val = x + 1
                
                # 2. Adım: Değişen biti (Lowbit) bul.
                # 24 (11000) -> Lowbit 8 (1000)
                lowbit = next_val & -next_val
                
                # 3. Adım: Lowbit'in yarısını x'ten çıkar.
                # 8 >> 1 = 4.
                # 23 - 4 = 19. (19 -> 10011. 19 OR 20 = 23. Doğru ve minimum.)
                ans.append(x - (lowbit >> 1))
                
        return ans