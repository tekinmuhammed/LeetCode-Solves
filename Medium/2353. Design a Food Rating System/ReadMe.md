# 🍲 LeetCode 2353 - Design a Food Rating System

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2353](https://leetcode.com/problems/design-a-food-rating-system)

---

## Problem Description

Design a food rating system that can do the following:

- **Initialization:**  
  Given three lists `foods`, `cuisines`, and `ratings`:
  - `foods[i]` is the name of the `i-th` food.
  - `cuisines[i]` is the type of cuisine of the `i-th` food.
  - `ratings[i]` is the rating of the `i-th` food.

- **Operations:**
  1. `changeRating(food, newRating)` – Updates the rating of the given food.
  2. `highestRated(cuisine)` – Returns the name of the highest-rated food of a particular cuisine.  
     - If multiple foods have the same highest rating, return the lexicographically smaller name.

---

## Example

### Input
```python
foods = ["kimchi","miso","sushi","moussaka","ramen","bulgogi"]
cuisines = ["korean","japanese","japanese","greek","japanese","korean"]
ratings = [9,12,8,15,14,7]

foodRatings = FoodRatings(foods, cuisines, ratings)
foodRatings.highestRated("korean")   # "kimchi"
foodRatings.highestRated("japanese") # "ramen"
foodRatings.changeRating("sushi", 16)
foodRatings.highestRated("japanese") # "sushi"
foodRatings.changeRating("ramen", 16)
foodRatings.highestRated("japanese") # "ramen"
```

### Output
```python
"kimchi"
"ramen"
"sushi"
"ramen"
```

### Approach

We need efficient lookups and updates, so we use multiple hash maps and a sorted data structure:

- `food_rating_map` → maps each food to its rating

- `food_cuisine_map` → maps each food to its cuisine

- `cuisine_food_map` → maps each cuisine to a SortedSet of foods, sorted by:

- - primary key: `-rating` (higher ratings come first)

- - secondary key: `food name` (lexicographically smaller first)

### Operations:

- `changeRating(food, newRating)`

- - Remove the old `(rating, food)` from its cuisine’s set

- - Update the rating

- - Insert the new `(rating, food)` back into the set

- `highestRated(cuisine)`

- - Simply return the first element from the sorted set of that cuisine

## Complexity
- **Time Complexity:**

- - **changeRating**: `O(log n)` (for SortedSet remove/insert)

- - **highestRated**: `O(1)`

- **Space Complexity:** `O(n)` (storing foods, cuisines, ratings)

### Tags
`design`, `heap`, `hashmap`, `sortedset`, `data-structures`