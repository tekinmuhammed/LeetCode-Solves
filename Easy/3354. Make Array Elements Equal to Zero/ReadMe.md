# ⚙️ LeetCode 3354. Make Array Elements Equal to Zero  

**Difficulty:** Easy
**Link:** [LeetCode 3354](https://leetcode.com/problems/make-array-elements-equal-to-zero/description/)

---

## 💡 Problem Description  

Bir tamsayı dizisi `nums` veriliyor.  
Her hamlede, dizideki bir sıfır elemanından başlayarak, bir yöne (sola veya sağa) doğru gidilir ve  
her adımda o yöndeki her bir eleman 1 azaltılır.  

Amaç:  
Dizideki **tüm elemanları 0 yapmak** için, hangi başlangıç konumları (`curr`) ve hareket yönü (sol/sağ) kombinasyonlarının **geçerli** olduğunu saymak.  

---

## 🧩 Example 1  

**Input:**  
```python
nums = [1, 0, 2, 0, 3]
```

**Output:**
```python
2
```

**Explanation:**

- `nums[1] = 0` → Sol taraf [1] ve sağ taraf [2, 0, 3].

- - Prefix sum = 1

- - Suffix sum = 5

- - |1 - 5| > 1 → Geçersiz.

- `nums[3] = 0` → Sol taraf [1, 0, 2], sağ taraf [3]

- Prefix sum = 3

- Suffix sum = 3

- |3 - 3| = 0 → Geçerli (2 yön)

Toplam geçerli seçim sayısı = 2

### 🧠 Approach

1. Prefix ve Suffix toplamlarını takip et.

- - `prefix_sum`: i’nin solundaki toplam

- - `suffix_sum`: i’nin sağındaki toplam

2. Sıfır olan her `nums[i]` konumu için:

- - `diff = |prefix_sum - suffix_sum|`

- - Eğer `diff <= 1` ise:

- - - `diff == 0` → her iki yön geçerli → `+2`

- - - `diff == 1` → sadece büyük toplam yönü geçerli → `+1`

3. Tüm geçerli kombinasyonları topla.

### 🧮 Time & Space Complexity
| İşlem                    | Zaman | Alan |
| ------------------------ | ----- | ---- |
| Tüm diziyi 1 kez dolaşma | O(n)  | O(1) |

### 💻 Code Implementation
```python
class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        """
        nums dizisindeki tüm elemanları sıfıra eşitleyen geçerli başlangıç (curr) 
        ve hareket yönü kombinasyonlarının sayısını döndürür.
        """
        n = len(nums)
        valid_selections = 0
        total_sum = sum(nums)
        suffix_sum = total_sum
        prefix_sum = 0

        for i in range(n):
            suffix_sum -= nums[i] 
            if nums[i] == 0:
                diff = abs(prefix_sum - suffix_sum)
                if diff <= 1:
                    if diff == 0:
                        valid_selections += 2
                    elif diff == 1:
                        valid_selections += 1
            prefix_sum += nums[i]

        return valid_selections
```

### 🧪 Example Test
```python
solution = Solution()

print(solution.countValidSelections([1, 0, 2, 0, 3]))  
# Output: 2

print(solution.countValidSelections([2, 3, 4, 0, 4, 1, 0]))  
# Output: 0
```

### 🏁 Summary
- ✔ Prefix ve suffix toplam farkı ≤ 1 koşulu kontrol edilir
- ✔ diff == 0 → 2 yön, diff == 1 → 1 yön geçerlidir
- ✔ Tek geçişte verimli hesaplama (O(n))

**Tags:** `Prefix-Sum`, `Simulation`, `Array`  