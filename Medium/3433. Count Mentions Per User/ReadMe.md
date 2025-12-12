# 3433. Count Mentions Per User

**Difficulty:** Medium
**Problem Link:** [LeetCode 3433](https://leetcode.com/problems/count-mentions-per-user/description/)

## 🧩 Problem Summary
Elimizde üç tür event var:

- **OFFLINE t u** → Kullanıcı `u`, zaman `t`’de çevrimdışı olur ve **60 birim** süre çevrimdışı kalır.
- **MESSAGE t ALL** → Tüm kullanıcılara mention.
- **MESSAGE t HERE** → Sadece şu an **çevrimiçi** olanlara mention.
- **MESSAGE t id5 id12 ...** → Belirli kullanıcı IDs’ine mention.

Amaç: Her kullanıcı için toplam mention sayısını döndürmek.

---

## 🔑 Key Rules
1. Olaylar sırayla gelmeyebilir → **timestamp’e göre sıralamak gerekiyor**.
2. Aynı timestamp’te:
   - **OFFLINE önce**, sonra **MESSAGE** işlenmeli.
3. OFFLINE olan kullanıcı tekrar **ts + 60** zamanında çevrimiçi olur.
4. Kullanıcı çevrimiçi olma durumu:
```python
ts >= online_time[u]
```

### 🧠 Solution Strategy

**Event'leri sıralama**
    Olayları şu kritere göre sıralıyoruz:

1. Zaman (timestamp)

2. Event türü (OFFLINE önce → rank=0, MESSAGE sonra → rank=1)

- Bunun için:
```python
(timestamp, rank, event)
```
şeklinde tuple oluşturup sort yapıyoruz.

**State Management**
- `online_time[u] = tekrar online olacağı zaman`

- Başlangıçta herkes online:
```python
online_time = [0] * numberOfUsers
```
- `mentions[u] = toplam mention sayısı`

**MESSAGE durumları**
- `"ALL"` → Herkesi 1 artır.

- `"HERE"` → Sadece şu an çevrimiçi olanları.

- `"idX"` listesi → Yalnızca verilen ID'leri artır.

### 🕒 Time Complexity
    Event sayısı **E**, kullanıcı sayısı **N**.

- Sıralama → O(E log E)

- İşleme:

- ALL → O(N)

- HERE → O(N)

- id listesi → O(#ids)

    Worst case: **O(E·N)**
→ Bu problem için kabul edilebilir.

### ✅ Code
```python
class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        # Prepare sortable event list
        processed_events = []
        for event in events:
            event_type = event[0]
            timestamp = int(event[1])
            rank = 0 if event_type == "OFFLINE" else 1
            processed_events.append((timestamp, rank, event))
        
        processed_events.sort()

        mentions = [0] * numberOfUsers
        online_time = [0] * numberOfUsers  # when each user becomes online again

        for ts, rank, event in processed_events:
            event_type = event[0]
            
            if event_type == "OFFLINE":
                user_id = int(event[2])
                online_time[user_id] = ts + 60
            
            elif event_type == "MESSAGE":
                mention_string = event[2]
                
                if mention_string == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                        
                elif mention_string == "HERE":
                    for i in range(numberOfUsers):
                        if ts >= online_time[i]:
                            mentions[i] += 1
                            
                else:
                    ids = mention_string.split()
                    for id_str in ids:
                        uid = int(id_str[2:])
                        mentions[uid] += 1
                        
        return mentions
```