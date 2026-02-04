# 3640. Trionic Array II

**Difficulty:** Hard  
**Link:** [LeetCode 3640](https://leetcode.com/problems/trionic-array-ii/description/)

---

## Problem Özeti

Bir dizi **trionic** olarak adlandırılırsa şu yapıyı sağlamalıdır:

1. **Strictly increasing**
2. **Strictly decreasing**
3. **Strictly increasing**

Ek şartlar:
- Üç segment de **en az bir eleman** içermeli
- Segmentler **bitişik (contiguous)** olmalı
- Amaç: bu yapıyı sağlayan **herhangi bir alt dizinin maksimum toplamını** bulmak

---

## Çözüm Fikri

Bu problemde:

- Diziyi soldan sağa geziyoruz
- Her başlangıç noktası için:
  1. İlk artan segmenti buluyoruz
  2. Ardından azalan segmenti buluyoruz
  3. Son olarak tekrar artan segmenti kontrol ediyoruz
- Eğer üç faz da geçerliyse:
  - Ortadaki **zorunlu çekirdek kısmı** alıyoruz
  - Sol ve sağdaki artan segmentlerden **en kârlı alt parçayı** seçiyoruz
- Global maksimumu güncelliyoruz

Bu yaklaşım:
- Brute force değildir
- Sliding window + greedy kombinasyonu kullanır
- Lineer zamana çok yakındır

---

## Kod

```python
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")
        i = 0

        while i < n:
            j = i + 1
            res = 0

            # 1) first segment: strictly increasing
            while j < n and nums[j - 1] < nums[j]:
                j += 1
            p = j - 1

            # increasing segment yoksa
            if p == i:
                i += 1
                continue

            # 2) second segment: strictly decreasing
            res += nums[p] + nums[p - 1]
            while j < n and nums[j - 1] > nums[j]:
                res += nums[j]
                j += 1
            q = j - 1

            # geçersiz decreasing veya 3. segment mümkün değilse
            if q == p or q == n - 1 or (j < n and nums[j] <= nums[q]):
                i = q
                continue

            # 3) third segment: strictly increasing
            res += nums[q + 1]

            # sağ tarafta maksimum katkıyı bul
            max_sum = 0
            curr_sum = 0
            k = q + 2
            while k < n and nums[k] > nums[k - 1]:
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
                k += 1
            res += max_sum

            # sol tarafta maksimum katkıyı bul
            max_sum = 0
            curr_sum = 0
            for k in range(p - 2, i - 1, -1):
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
            res += max_sum

            # cevabı güncelle
            ans = max(ans, res)
            i = q

        return ans
```

Zaman ve Alan Karmaşıklığı
Zaman: O(n) (pratikte)

Alan: O(1)