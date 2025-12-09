# 1925. Count Square Sum Triples

**Difficulty:** Easy
**Problem Link:** [LeetCode 1925](https://leetcode.com/problems/count-square-sum-triples/description/)

### Amaç:  
`1 ≤ a, b, c ≤ n` olacak şekilde  
**a² + b² = c²** şartını sağlayan *tüm sıralı* (a, b, c) üçlülerini saymak.

---

# 🟩 Your Code

```python
class Solution(object):
    def countTriples(self, n):
        count = 0
        
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c2 = a*a + b*b
                c = int(c2**0.5)
                
                if c <= n and c*c == c2:
                    count += 1
                    
        return count
```

### 🧠 How It Works
**✔ Brute-force çift döngü ile tüm `a`, `b` değerleri geziliyor.**

- Her ikili için:

1. `c² = a² + b²` hesaplanır

2. `c = √(c²)` alınır

3. Eğer hem karekök tam sayı ise Pythagorean triple bulunmuştur

4. Eğer `c ≤ n` ise geçerlidir → `count++`

### 🧮 Time Complexity

- Çift döngü → `O(n²)`