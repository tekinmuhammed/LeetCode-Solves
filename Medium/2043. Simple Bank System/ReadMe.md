# 🏦 LeetCode 2043. Simple Bank System  

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2043](https://leetcode.com/problems/simple-bank-system/description/)

---

## 💡 Problem Description  
Bir banka sistemi tasarlamamız isteniyor.  

Banka sisteminde:  
- Her müşteri bir **hesaba** sahiptir.  
- Hesap bakiyeleri `balance` listesi ile tutulur.  
- Aşağıdaki işlemler desteklenmelidir:  
  1. `transfer(account1, account2, money)` → Hesaplar arası para transferi  
  2. `deposit(account, money)` → Para yatırma  
  3. `withdraw(account, money)` → Para çekme  

Her işlem geçerli değilse (`account` numarası hatalıysa veya bakiye yetersizse) `False` döndürülür.  
Geçerliyse işlem yapılır ve `True` döndürülür.  

---

## 🧠 Approach  
Bu problem saf bir **sınıf tasarımı (class design)** sorusudur.  

Yapılacak adımlar:
1. `Bank` sınıfı tanımlanır, `__init__` metodu ile hesap bakiyeleri kaydedilir.  
2. Her işlem için ayrı metot tanımlanır:
   - `transfer`: Hem hesap geçerliliği hem de bakiye yeterliliği kontrol edilir.  
   - `deposit`: Hesap geçerliyse belirtilen miktar eklenir.  
   - `withdraw`: Hesap geçerliyse ve yeterli bakiye varsa belirtilen miktar düşülür.  
3. Hesaplar 1-indekslidir (yani 1. hesap `balance[0]`'a denk gelir).  

---

## 🧩 Example  

**Input:**  
```python
bank = Bank([10, 100, 20, 50, 30])
bank.withdraw(3, 10)
bank.transfer(5, 1, 20)
bank.deposit(5, 20)
bank.transfer(3, 4, 15)
bank.withdraw(10, 50)
```

**Output:**
```python
True
True
True
False
False
```

**Explanation:**

- Hesap 3’ten 10 çekilir → ✅

- Hesap 5’ten hesap 1’e 20 transfer edilir → ✅

- Hesap 5’e 20 yatırılır → ✅

- Hesap 3’ten hesap 4’e 15 transfer edilir (artık bakiyesi yetersiz) → ❌

- Hesap 10 mevcut değil → ❌

### 🧮 Time & Space Complexity
| Operation                     | Time | Space |
| ----------------------------- | ---- | ----- |
| deposit / withdraw / transfer | O(1) | O(1)  |


### 🧰 Code Implementation
```python
class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            account1 > len(self.balance)
            or account2 > len(self.balance)
            or self.balance[account1 - 1] < money
        ):
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance) or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
```

### 🏁 Summary
- ✔ Basit ve temiz bir class design örneği
- ✔ Tüm işlemler O(1) zamanda çalışır
- ✔ Hatalı hesap veya bakiye durumları doğru şekilde yakalanır

**Tags:** `Simulation`, `OOP (Object-Oriented Programming)`, `Design`  