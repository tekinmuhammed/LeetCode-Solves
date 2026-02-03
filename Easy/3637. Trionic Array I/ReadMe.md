## 3637. Trionic Array I

**Difficulty:** Easy  
**Link:** [LeetCode 3606](https://leetcode.com/problems/coupon-code-validator/description/)

---

Bu problem, dizinin **3 ardışık fazdan** oluşup oluşmadığını kontrol ediyor:

1. **Strictly increasing (kesin artan)**
2. **Strictly decreasing (kesin azalan)**
3. **Strictly increasing (kesin artan)**

Ve bu üç fazın **her biri en az 1 adım içermeli**.

---

## Trionic Array Nedir?

Bir dizi `nums` için:

- Önce değerler **artan**
- Sonra **azalan**
- En sonda tekrar **artan**
- Hiçbir yerde eşitlik yok (`<` ve `>` şart)
- Fazlar **boş olamaz**

Örnek:
```text
[1, 3, 5, 4, 2, 6, 8]
 ↑  ↑  ↓  ↓  ↑  ↑
```

### Kodun Adım Adım Analizi
**Başlangıç**
```python
n = len(nums)
i = 0
```

### 1️⃣ Strictly Increasing Fazı
```python
while i + 1 < n and nums[i] < nums[i + 1]:
    i += 1
```
- Artış bozulana kadar ilerliyorsun
**Kontroller:**
```python
if i == 0 or i == n - 1:
    return False
```
- `i == 0` → hiç artış yok
- `i == n-1` → dizi tamamen artan, diğer fazlar yok

### 2️⃣ Strictly Decreasing Fazı
```python
while i + 1 < n and nums[i] > nums[i + 1]:
    i += 1
```
- Azalış bozulana kadar ilerliyorsun
**Kontrol:**
```python
if i == n - 1:
    return False
```
- Dizi burada bittiyse → 3. faz yok

### 3️⃣ Strictly Increasing Fazı (Tekrar)
```python
while i + 1 < n and nums[i] < nums[i + 1]:
    i += 1
```
- Son artış fazı

### Final Kontrol ✅
```python
return i == n - 1
```
- Eğer dizinin sonuna tam olarak ulaşıldıysa:
- - ✔ Trionic
- Aksi halde:
- - ❌ Kurallardan biri bozulmuş

### Time Complexity ⭐
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`