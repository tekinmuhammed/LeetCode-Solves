# 🎬 LeetCode 1912 - Design Movie Rental System

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1912](https://leetcode.com/problems/design-movie-rental-system)

---

## Problem Description

You are asked to design a **movie renting system** that supports the following operations:

- The system has `n` shops numbered from `0` to `n - 1`.
- Each entry in `entries` represents a movie available in a shop with a price:
  - `entries[i] = [shop, movie, price]`.

The system should implement:

1. **`search(movie)`**  
   Returns up to 5 cheapest shops (by price, then by shop index) that have not rented out the given movie.

2. **`rent(shop, movie)`**  
   Rents out the given movie from the shop.

3. **`drop(shop, movie)`**  
   The customer returns the rented movie to the shop.

4. **`report()`**  
   Returns up to 5 cheapest rented movies in the system, sorted by `(price, shop, movie)`.

---

## Example

### Input
```python
movieRentingSystem = MovieRentingSystem(
    3,
    [[0,1,5],[0,2,6],[0,3,7],
     [1,1,4],[1,2,7],[2,1,5]]
)

movieRentingSystem.search(1)   # [1, 0, 2]
movieRentingSystem.rent(0, 1)
movieRentingSystem.report()    # [[0, 1]]
movieRentingSystem.drop(0, 1)
movieRentingSystem.search(1)   # [1, 0, 2]
```

### Output
```python
[1,0,2]
[[0,1]]
[1,0,2]
```

### Approach

We use efficient data structures to manage movies:

- `self.movies`: maps each `movie` → `SortedList` of `(price, shop)`
(stores all available movies in each shop)

- `self.sm_p`: dictionary mapping `(shop, movie)` → `price`
(for quick lookup of movie price in a shop)

- `self.rented`: `SortedList` of `(price, shop, movie)`
(keeps track of currently rented movies, sorted by required order)

### Operations:

- `search(movie)` → Get up to 5 cheapest available shops for that movie.

- `rent(shop, movie)` → Remove from available, add to rented.

- `drop(shop, movie)` → Move back from rented to available.

- `report()` → Return up to 5 cheapest rented movies.

This approach guarantees efficient operations with logarithmic complexity thanks to `SortedList`.

### Complexity

- **Time Complexity:**

- - `search`: O(1) (fetch first 5 from SortedList)

- - `rent/drop`: O(log n) (insert/remove in SortedList)

- - `report`: O(1) (fetch first 5 from SortedList)

- **Space Complexity**: `O(n)` (store all movies and rented info)

### Tags

`design`, `sortedlist`, `heap`, `hashmap`, `priority-queue`, `data-structures`