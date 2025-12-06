# 3578. Count Partitions With Max-Min Difference at Most K  

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3578](https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/description/)


### Bu problemde amaç:  
- Bir diziyi ardışık parçalara bölmek; her parçanın **(max - min ≤ k)** koşulunu sağlaması gerekir.  
- - Tüm geçerli bölme senaryolarının toplam sayısını bulmalıyız.

---

# 🧠 Core Idea

Bir parçanın geçerli olabilmesi için:
```python
max(subarray) - min(subarray) ≤ k
```

Bu da bize, her bitiş noktası `i` için:
- Parçanın başladığı en küçük `j` indeksini bulmamız gerektiğini söyler.

Yani `nums[j..i]` aralığı geçerli olmalı.

Bu geçerli aralık içinde, her `j` için:
```python
dp[i+1] += dp[j]
```

DP tanımı:
- `dp[i]`: `nums[:i]` alt dizisini geçerli şekilde bölmenin toplam yolu  
- `dp[0] = 1` (boş dizi için bir yol)

---

# 🚀 Efficient Approach in Your Code

### 1. **Monotonic Deques (Sliding Window Max/Min)**
- `max_q`: penceredeki maksimum değerlerin indeksini tutar  
- `min_q`: penceredeki minimum değerlerin indeksini tutar  
- Böylece `max - min` kontrolü O(1)'de yapılır.

Bu sayede `left` sınırını en sağa kadar iterek:
```python
nums[left..i]
```
→ geçerli minimum başlangıç bölgeyi belirliyorsun.

---

### 2. **DP Transition**
Her `i` için:
```python
dp[i+1] = dp[left] + dp[left+1] + ... + dp[i]
```

Bu toplamı hızlı almak için prefix sum kullanıyorsun:
```python
dp[i+1] = prefix_dp[i+1] - prefix_dp[left]
```

**Bu yapı:**
- Sliding window → O(n)
- dp + prefix sum → O(n)
- Total → **O(n)**

---

# 🟩 Code Review (Your Solution — Clean & Correct)

```python
from collections import deque

class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        prefix_dp = [0] * (n + 2)
        prefix_dp[1] = 1
        
        min_q = deque()
        max_q = deque()
        
        left = 0
        
        for i in range(n):
            while max_q and nums[max_q[-1]] <= nums[i]:
                max_q.pop()
            max_q.append(i)
            
            while min_q and nums[min_q[-1]] >= nums[i]:
                min_q.pop()
            min_q.append(i)
            
            while nums[max_q[0]] - nums[min_q[0]] > k:
                left += 1
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()
            
            current_ways = (prefix_dp[i+1] - prefix_dp[left]) % MOD
            dp[i+1] = current_ways
            
            prefix_dp[i+2] = (prefix_dp[i+1] + current_ways) % MOD
            
        return dp[n]
```

### 📝 Final Evaluation
- ✔ Doğru
- ✔ Optimal (O(n))