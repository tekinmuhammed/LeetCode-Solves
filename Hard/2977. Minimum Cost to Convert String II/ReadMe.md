## 2977. Minimum Cost to Convert String II

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2977](https://leetcode.com/problems/minimum-cost-to-convert-string-ii/description/)

---

### Problem Özeti

- Elimizde:
  - `source` ve `target` stringleri (aynı uzunlukta)
  - Dönüşüm kuralları:
    - `original[i] → changed[i]` maliyeti `cost[i]`
- Kurallar **substring bazlı** çalışır (tek karakter olmak zorunda değil)
- Amaç:
  - `source` → `target` dönüşümünü **minimum toplam maliyetle** yapmak
- Mümkün değilse `-1`

---

## Çözümün Ana Fikri 💡

Bu problem 3 ana katmandan oluşur:

### 1️⃣ Trie (Prefix Tree)
- `original` ve `changed` içindeki tüm stringleri Trie’ye ekliyorsun
- Her **kelime sonu** bir **ID** alıyor
- Böylece:
  - `source[j:i]` ve `target[j:i]` aynı anda Trie üzerinde ilerletilebiliyor

👉 Bu sayede **aynı uzunluktaki substring dönüşümleri** hızlıca yakalanıyor

---

### 2️⃣ Floyd–Warshall (All-Pairs Shortest Path)

- Her `original → changed` dönüşümü bir **directed edge**
- Ama:
  - A → B → C zinciri, A → C’den daha ucuz olabilir
- Bu yüzden:
  - Tüm dönüşümler için **minimum maliyetleri** önceden hesaplıyorsun

```text
dist[x][y] = x kelimesini y kelimesine çevirmenin min maliyeti
```
✔️ Bu adım olmazsa, DP sırasında eksik/yanlış maliyet hesaplanır

### 3️⃣ Dynamic Programming (String Üzerinde)
`dp[i]:`
- `source[0:i]` → `target[0:i]` dönüşümünün minimum maliyeti
Geçişler:

### ✅ Karakter Karakter Geçiş
```python
source[i] == target[i]
dp[i+1] = min(dp[i+1], dp[i])
```

### 🔁 Substring Dönüşümü
- `j`’den başlayarak:
- - `source[j:i]` ve `target[j:i]` Trie üzerinde ilerletilir
- - Eğer ikisi de bir kelime bitişiyse:
```python
dp[i+1] = min(dp[i+1], dp[j] + dist[u][v])
```

### Kodun Yapısal Analizi 🧠
**Trie Yapısı**
```python
child[node][c]  # Trie geçişleri
tid[node]       # Bu node bir kelime bitişiyse ID
```
- `add(word):`
- - Trie’ye kelime ekler
- - Eğer yeni kelimeyse yeni bir ID üretir

### Floyd–Warshall
```python
for k in range(P):
    for i in range(P):
        for j in range(P):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```
- `P`: toplam farklı kelime sayısı
- `dist[i][j]`: i → j minimum dönüşüm maliyeti

### DP Geçişi (En Kritik Kısım)
```python
for j in range(n):
    if dp[j] >= INF:
        continue
```
- Trie üzerinde **aynı anda** ilerleme:

```python
u = child[u][s_arr[i]]
v = child[v][t_arr[i]]
```
- Eğer ikisi de kelime bitişiyse:

```python
dp[i+1] = min(dp[i+1], dp[j] + dist[uid][vid])
```
✔️ Bu kısım problemin “II” seviyesini yapan ana fark

### Zaman & Alan Karmaşıklığı
- **Zaman**
- - Trie kurma: `O(total_length)`
- - Floyd–Warshall: `O(P³)`
- - DP + Trie gezme: `O(n²)`

- **Alan**
- - Trie: `O(total_length)`
- - Dist matrix: `O(P²)`
- - DP: `O(n)`