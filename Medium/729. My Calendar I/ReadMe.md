# 📅 LeetCode 729 - My Calendar I

**Difficulty:** Medium  
**Problem Link:** [LeetCode 729](https://leetcode.com/problems/my-calendar-i)

---

## 📘 Problem Description

You are implementing a **calendar booking system**. Create a class `MyCalendar` that can book a new event if it does **not overlap** with existing ones.

Each booking is represented by a half-open interval `[start, end)` — it includes `startTime`, but **not** `endTime`.

Implement the `MyCalendar` class:

- `MyCalendar()` Initializes the calendar.
- `book(start, end)` Returns `True` if the event can be added to the calendar without causing a double booking. Otherwise, return `False`.

---

## 🧪 Example

```python
calendar = MyCalendar()
calendar.book(10, 20)  # returns True
calendar.book(15, 25)  # returns False (overlaps with 10–20)
calendar.book(20, 30)  # returns True
```

### 🚀 Approach

To handle new bookings:

1. Maintain a list of existing bookings.

2. For each new booking, check for overlaps using:

```python
if max(s, start) < min(e, end):  # Overlap condition
```

3. If no overlap is found, append the booking to the list.

### ⏱️ Complexity

- **Time Complexity:** `O(n)` per booking (linear scan through existing bookings)

- **Space Complexity:** `O(n)` for storing the intervals


### 🏷️ Tags

`interval`, `calendar`, `design`, `greedy`, `simulation`