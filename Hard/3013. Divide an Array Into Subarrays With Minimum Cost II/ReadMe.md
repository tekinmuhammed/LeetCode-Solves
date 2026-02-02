## 3013. Divide an Array Into Subarrays With Minimum Cost II

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3013](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/description/)

---

Bu soru, **3010’un genelleştirilmiş ve zorlaştırılmış hali**.  
Burada hem `k` hem de `dist` kısıtları devreye giriyor.

---

## Problem Özeti

- `nums` dizisi veriliyor
- Seçilecek alt dizinin:
  - Toplam **k elemanı** olacak
  - İlk eleman **zorunlu olarak `nums[0]`**
- Seçilen diğer elemanlar için:
  - Bir **pivot index `i`** seçiliyor
  - Pivot `nums[i]`
  - Kalan `k-2` eleman **[i+1, i+dist] aralığından** seçilmeli
- Amaç:
  - `nums[0] + nums[i] + (k-2 elemanın toplamı)` → **minimum**

---

## Yüksek Seviye Fikir 🧠

Her pivot `i` için:

1. `nums[0]` → sabit
2. `nums[i]` → pivot
3. `[i+1 ... i+dist]` aralığından **en küçük `k-2` elemanı** seç

👉 Asıl zor kısım:
- Kayar pencere içinde **dinamik olarak en küçük K elemanı tutmak**

Bunu da:
- **İki heap + sliding window + lazy deletion** ile çözmüşsün  
- Bu, LeetCode **Hard** seviyesinde “kitaplık” bir çözüm 👏

---

## Özel Durum: `k == 2`

```python
if K == 0:
    return base_cost + min(nums[1:])
```
- `k = 2` → sadece `nums[0]` ve **bir tane daha**
- `dist` kısıtı anlamsız hale gelir
- Doğrudan minimumu almak **doğru ve optimal**

### Veri Yapıları 🧩
**Heap’ler**
- `L` → Max-Heap (en küçük `K` elemanı tutar)
- `R` → Min-Heap (geri kalanlar)

Amaç:
- `L` her zaman seçilecek `k-2` en küçük elemanı içerir
- `L_sum` → bu elemanların toplamı (O(1) maliyet hesabı)

### Lazy Deletion (Çok Kritik) ⚠️
Heap’ten rastgele eleman silemediğimiz için:
```python
rem_L = defaultdict(int)
rem_R = defaultdict(int)
```
- Silinmesi gereken elemanları işaretliyorsun
- Heap’in tepesine gelince gerçekten siliyorsun

### `add(val)` – Eleman Ekleme
Mantık:
1. Önce `L`’ye ekle
2. Eğer `L_size > K`:
- - En büyük elemanı `R`’ye at
3. Gerekirse `L` ve `R` arasında swap yaparak dengeyi koru
Amaç:
- `L` = her zaman **en küçük K eleman**

### `remove(val)` – Eleman Çıkarma
1. Elemanın **hangi heap’te olduğunu tahmin ediyorsun**
2. Lazy removal ile işaretliyorsun
3. Eğer `L` küçülürse:
- - `R`’den takviye alıyorsun
Bu sayede:
- Sliding window düzgün çalışıyor
- Heap bozulmuyor

### Sliding Window Mantığı 🪟
Başlangıç havuzu:
```python
nums[2 ... dist+1]
```
Sonra pivot `i` için:
```python
current_cost = nums[0] + nums[i] + L_sum
```
Ardından pencere kayıyor:
- Çıkan: `nums[i+1]`
- Giren: `nums[i+dist+1]`

### Zaman & Alan Karmaşıklığı ⏱️
- **Time:** `O(n log n)`
- **Space:** `O(n)`