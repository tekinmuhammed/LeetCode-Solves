# 756. Pyramid Transition Matrix

**Difficulty:** Medium  
**Problem Link:** [LeetCode 756](https://leetcode.com/problems/pyramid-transition-matrix/description/)

---

## 🧩 Problem Özeti

- Elimizde:
  - `bottom`: Piramidin **en alt satırı**
  - `allowed`: Üç harften oluşan kurallar (`ABC`)
- Kural anlamı:
  - Eğer altta `A` ve `B` yan yanaysa, üstüne `C` konabilir

🎯 Amaç:
> Piramidi **üstte tek bir harf kalana kadar** kurmak **mümkün mü?**

---

## 🧠 Temel Yaklaşım

Bu problem:
- **Backtracking (DFS)**
- + **Memoization (tekrarları engelleme)**  
ile çözülür.

Çünkü:
- Her seviyede birçok olası üst satır üretilebilir
- Aynı alt diziler tekrar tekrar denenebilir

---

## 🗂️ Adım 1: Kuralları Haritalama

```python
mp = defaultdict(list)
for a in allowed:
    mp[a[0] + a[1]].append(a[2])
```
📌 Amaç:
- `(sol, sağ)` ikilisinden hangi üst harf(ler) üretilebilir?

Örnek:
```python
"ABC" → mp["AB"] = ["C"]
```

Yani:
```python
mp["AB"] = ["C", "D", ...]
```

### 🧠 Memoization
```python
memo = set()
```
- Daha önce **başarısız olduğu kanıtlanmış** `curr` string’lerini tutar
- Aynı durumu tekrar denememek için 💡

### 🔁 DFS (Derinlik Öncelikli Arama)
```python
def dfs(curr):
```

### ✅ Base Case
```python
if len(curr) == 1:
    return True
```
- Piramit başarıyla tamamlandı 🎉

### ❌ Daha Önce Denendiyse
```python
if curr in memo:
    return False
```

### 🏗️ Bir Üst Satırı Oluşturma (Backtracking)
```python
def build_next(i, path):
```
Bu fonksiyon:
- `curr` satırından
- olası **üst satırları** karakter karakter oluşturur

### 🔚 Üst Satır Tamamlandıysa
```python
if i == len(curr) - 1:
    return dfs(path)
```
- Yeni satır hazır
- Bir üst seviyeye geçilir

### ❌ Kural Yoksa
```python
key = curr[i] + curr[i + 1]
if key not in mp:
    return False
```
- Bu ikili için üst harf yok → yol kapanır 🚫

### 🔄 Olası Tüm Harfleri Dene
```python
for c in mp[key]:
    if build_next(i + 1, path + c):
        return True
```
- Bir tanesi bile başarılıysa → zincirleme başarı ✅

### 🧱 DFS Sonuç Kontrolü
```python
if not build_next(0, ""):
    memo.add(curr)
    return False
return True
```
- Hiçbir yol çalışmadıysa:
- - `curr` artık imkansız
- - memo’ya eklenir

### 🧪 Örnek Akış
```python
bottom = "BCD"
allowed = ["BCG", "CDE", "GEA", "FFF"]
```
1. "BCD"
2. "GE"
3. "A"
    ✅ True

### ⏱️ Zaman & Alan Karmaşıklığı
- **⏳ Zaman**
- - En kötü durumda **exponential**
- - Ama:
- - - memoization ile ciddi şekilde kırpılır

- **🧠 Alan**
- - Recursion stack + memo