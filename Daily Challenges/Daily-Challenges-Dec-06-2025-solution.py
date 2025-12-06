# 3578. Count Partitions With Max-Min Difference at Most K

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3578](https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/description/)

# 🧠 Problem Description
# [Github LeetCode 3578. Count Partitions With Max-Min Difference at Most K](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3578.%20Count%20Partitions%20With%20Max-Min%20Difference%20at%20Most%20K)

from collections import deque

class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        # dp[i]: nums dizisinin ilk i elemanını (nums[0...i-1]) 
        # geçerli alt dizilere ayırma yollarının sayısı.
        # dp[0] = 1 (Boş dizi için 1 yol - hiç bölmemek)
        dp = [0] * (n + 1)
        dp[0] = 1
        
        # prefix_dp[i]: dp[0] + dp[1] + ... + dp[i-1] toplamını tutar.
        # Bu sayede belirli bir aralıktaki dp değerlerinin toplamını O(1)'de buluruz.
        prefix_dp = [0] * (n + 2)
        prefix_dp[1] = 1  # prefix_dp[1] = dp[0]
        
        # Monotonik kuyruklar: 
        # min_q penceredeki minimum elemanların indekslerini, 
        # max_q maksimum elemanların indekslerini tutar.
        min_q = deque()
        max_q = deque()
        
        left = 0 # Geçerli pencerenin sol sınırı
        
        for i in range(n):
            # 1. Max Deque Güncelleme:
            # Yeni gelen eleman (nums[i]) kuyruktaki elemanlardan büyükse,
            # o elemanlar artık maksimum olamaz, onları çıkar.
            while max_q and nums[max_q[-1]] <= nums[i]:
                max_q.pop()
            max_q.append(i)
            
            # 2. Min Deque Güncelleme:
            # Yeni gelen eleman kuyruktakilerden küçükse, onları çıkar.
            while min_q and nums[min_q[-1]] >= nums[i]:
                min_q.pop()
            min_q.append(i)
            
            # 3. Pencereyi Daraltma (Koşul Sağlanmıyorsa):
            # Eğer penceredeki max - min > k ise, sol sınırı (left) artır.
            while nums[max_q[0]] - nums[min_q[0]] > k:
                left += 1
                # Eğer max veya min indeksleri pencerenin dışında kaldıysa kuyruktan at.
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()
            
            # 4. DP Geçişi:
            # Son parça nums[j...i] olabilir, burada j değeri 'left' ile 'i' arasında olabilir.
            # Bu durumda dp[i+1] = sum(dp[left], dp[left+1], ..., dp[i])
            # Bunu prefix_dp kullanarak hızlıca hesaplarız:
            # Toplam = prefix_dp[i+1] - prefix_dp[left]
            
            current_ways = (prefix_dp[i+1] - prefix_dp[left]) % MOD
            dp[i+1] = current_ways
            
            # 5. Prefix DP Güncelleme
            prefix_dp[i+2] = (prefix_dp[i+1] + current_ways) % MOD
            
        return dp[n]