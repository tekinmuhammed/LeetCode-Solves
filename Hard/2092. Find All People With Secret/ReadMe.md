# 2092. Find All People With Secret

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2092](https://leetcode.com/problems/find-all-people-with-secret/description/)

---

## 🧩 Problem Özeti

- Toplam **n kişi** var.
- Bazı kişiler belirli zamanlarda **toplantılar (meetings)** yapıyor.
- **0. kişi** ve `firstPerson`, **zaman 0’da** bir sırrı biliyor.
- Bir kişi, **sırrı bildiği zamandan sonra** gerçekleşen bir toplantıda sırrı karşı tarafa aktarabiliyor.
- Amaç: **en sonunda sırrı bilen herkesin listesini** bulmak.

---

## 🧠 Temel Fikir

Bu problem aslında:

> **Zaman kısıtlı bir BFS / Dijkstra problemi**

olarak modellenebilir.

### Neden?
- Her toplantı bir **kenar**
- Toplantı zamanı → **kenar ağırlığı**
- Bir kişiden diğerine ancak **zaman geriye gitmeden** geçebiliriz

➡️ Bu yüzden **min-heap (priority queue)** ile ilerleyen bir BFS kullanıyoruz.

---

## 🔧 Adım Adım Çözüm

### 1️⃣ Graph Oluşturma

```python
graph = defaultdict(list)
for x, y, t in meetings:
    graph[x].append((t, y))
    graph[y].append((t, x))
```
📌 Her kişi için:

- `(toplantı zamanı, görüştüğü kişi)` tutulur

- Graph **undirected** (iki yönlü)

### 2️⃣ Başlangıç Durumu
```python
pq = []
heappush(pq, (0, 0))
heappush(pq, (0, firstPerson))
```
- **0. kişi ve firstPerson**

- Zaman `0`’da sırrı biliyor

- Priority Queue: `(sırrı öğrenme zamanı, kişi)`

### 3️⃣ Visited Dizisi
```python
visited = [False] * n
```
📌 Bir kişi **ilk kez kuyruktan çıktığında** sırrı öğrenmiş kabul edilir.
Sonrasında tekrar işlemeyiz.

### 4️⃣ Zaman Kısıtlı BFS (Dijkstra Mantığı)
```python
while pq:
    time, person = heappop(pq)
    if visited[person]:
        continue
    visited[person] = True
```
- En **erken zamanda** sırrı öğrenen kişi işlenir

- Aynı kişiyi tekrar işlemeyiz

### 5️⃣ Komşulara Yayılım
```python
for t, next_person in graph[person]:
    if not visited[next_person] and t >= time:
        heappush(pq, (t, next_person))
```
📌 Kritik koşul:

- Toplantı zamanı `t`, kişinin sırrı öğrendiği zamandan **büyük veya eşit** olmalı

➡️ Aksi halde geçmişteki bir toplantıyla sır aktarılamaz ❌

### 6️⃣ Sonuç
```python
return [i for i in range(n) if visited[i]]
```
- `visited == True` olan herkes sırrı öğrenmiştir ✅

### ⏱️ Zaman & Alan Karmaşıklığı

- **Zaman:** `O((n + m) log n)`
- - `m = meetings sayısı`
- Priority Queue kullanımı nedeniyle `log n`

- **Alan:** `O(n + m)`