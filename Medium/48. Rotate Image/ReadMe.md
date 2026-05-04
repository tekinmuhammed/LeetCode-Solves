# 48. Rotate Image

**Zorluk:** Medium
**Problem Linki:** [LeetCode 48](https://leetcode.com/problems/rotate-image/description/?)

---

## Problem Açıklaması

Size $n \times n$ boyutlarında bir matris veriliyor. Bu matrisi saat yönünde **90 derece** döndürmeniz isteniyor. En önemli kısıtlama, bu işlemin **in-place** (yerinde) yapılmasıdır. Yani yeni bir matris oluşturamazsınız, değişikliği doğrudan size verilen matris üzerinde yapmalısınız.

---

## Yaklaşım: Transpoz ve Satır Tersleme

Matrisi doğrudan döndürmeye çalışmak karmaşık indeks hesaplamaları gerektirebilir. Ancak lineer cebirdeki iki basit işlemi ardışık yaparak aynı sonucu elde edebiliriz:

### İzlenecek Adımlar:
1.  **Transpoz (Devrik):** Matrisin satırlarını sütun, sütunlarını satır yapın. Bu işlem ana diyagonal (sol üstten sağ alta uzanan çizgi) üzerindeki elemanları sabit tutarken diğerlerini karşılıklı takas eder.
    *   Matematiksel olarak: $(i, j) \to (j, i)$
2.  **Satır Tersleme:** Her bir satırı kendi içinde yatay olarak ters çevirin.
    *   Matematiksel olarak: $(j, i) \to (j, n - 1 - i)$



Bu iki işlemin birleşimi sonucunda elemanlar tam olarak saat yönünde 90 derece dönmüş konuma gelir.

---

## Kod

```python
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None (Matrisi yerinde değiştirir)
        """
        n = len(matrix)
        
        # 1. Adım: Transpoz (Diyagonal üzerinden yansıtma)
        for i in range(n):
            # j'yi i + 1'den başlatarak sadece üst üçgeni dolaşırız
            # Böylece elemanları bir kez takas etmiş oluruz
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2. Adım: Her satırı ters çevirme (Yatay yansıtma)
        for row in matrix:
            row.reverse()
```

## Karmaşıklık Analizi

- **Zaman Karmaşıklığı**: $O(n^2)$
Matristeki her bir hücreyi transpoz ve tersleme işlemleri sırasında sabit sayıda (en fazla 2 kez) ziyaret ediyoruz. $n \times n$ matris için bu işlem karesel zaman alır.

- **Alan Karmaşıklığı:** $O(1)$
Herhangi bir ek veri yapısı veya kopya matris kullanmadık. Tüm işlemler orijinal matrisin belleği üzerinde gerçekleştirildi.

## Etiketler
`Array`, `Math`, `Matrix`, `In-place`, `Two-Pointers`