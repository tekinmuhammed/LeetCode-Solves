# 1339. Maximum Product of Splitted Binary Tree

**Difficulty:** Medium  
**Link:** [LeetCode 1339](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/)  

---

## 🧩 Problem Özeti

Bir **binary tree** veriliyor.  
Ağaçtan **tek bir kenarı keserek** ağacı iki parçaya ayırıyoruz.

🎯 Amaç:
> Oluşan iki alt ağacın **node değerleri toplamlarının çarpımını maksimize etmek**

Sonuç çok büyük olabileceği için:
- **`10^9 + 7` modunda** döndürülür.

---

## 🧠 Temel Fikir

Bir kenarı kestiğimizde:

- Bir taraf: bir **alt ağacın toplamı** → `s`
- Diğer taraf: geri kalan kısım → `total_sum - s`

➡️ Çarpım:  
\[
s \times (total\_sum - s)
\]

Dolayısıyla:
- Tüm **alt ağaç toplamlarını** biliyorsak
- Her biri için bu çarpımı hesaplayıp maksimumu seçebiliriz

---

## 🚀 Çözüm Stratejisi (DFS + Subtree Sum)

### 1️⃣ DFS ile alt ağaç toplamlarını hesapla
- Her düğüm için:
```python
subtree_sum = node.val + left_sum + right_sum
```
- Bu değeri bir listeye ekle

### 2️⃣ Toplam ağaç değerini öğren
- DFS dönüş değeri zaten `total_sum`

### 3️⃣ Tüm olası kesimler için maksimum çarpımı bul
- Her `s` için:
```python
s * (total_sum - s)
```

---

## ✅ Senin Kodun

```python
class Solution(object):
  def maxProduct(self, root):
      MOD = 10**9 + 7
      subtree_sums = []

      def dfs(node):
          if not node:
              return 0
          s = node.val + dfs(node.left) + dfs(node.right)
          subtree_sums.append(s)
          return s

      total_sum = dfs(root)
      max_product = 0

      for s in subtree_sums:
          max_product = max(max_product, s * (total_sum - s))

      return max_product % MOD
```

### 🔍 Neden Doğru?
- DFS ile **her olası kesimin** temsilcisi olan alt ağaçlar elde ediliyor
- Her kesim için doğru çarpım hesaplanıyor
- En büyük değer seçiliyor
✔️ Tüm kenarlar dolaylı olarak denenmiş oluyor

### 🧪 Örnek
**Ağaç:**
```python
        1
       / \
      2   3
     / \
    4   5
```
**Alt ağaç toplamları:**
- 4 → 4
- 5 → 5
- 2 → 11
- 3 → 3
- 1 → 15 (toplam)
**En iyi kesim:**
- `11 * (15 - 11) = 44`

### ⏱️ Karmaşıklık
- **Zaman:** `O(n)`

- **Alan:** `O(n)` (subtree_sums listesi + recursion stack)