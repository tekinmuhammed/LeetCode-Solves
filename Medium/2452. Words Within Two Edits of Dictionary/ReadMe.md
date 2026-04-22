# 2452. Words Within Two Edits of Dictionary

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2452](https://leetcode.com/problems/words-within-two-edits-of-dictionary/)

---

## Problem Description

You are given two string arrays, `queries` and `dictionary`. All words in both arrays have the same length.

In one **edit**, you can take a character from a word and change it to any other character.

Return a list of all strings from `queries` that have at most **two edits** between them and any word in `dictionary`. The order of the returned strings should match the order in the `queries` array.

---

## Approach: Brute Force Comparison (Hamming Distance)

Since all words have the same length and the constraints are relatively small, we can directly compare each query word against every word in the dictionary.

### Key Ideas:
1.  **Character-by-Character Comparison:** For each `query` and each word `s` in the `dictionary`, we iterate through their indices and count how many characters are different. This is essentially calculating the **Hamming Distance**.
2.  **Early Exit (Optional):** As soon as we find a word in the dictionary that matches the query within 2 edits, we add the query to our result list and stop checking other dictionary words for that specific query.
3.  **Preserving Order:** We iterate through `queries` in their original order to ensure the output list follows the required sequence.

---

## Code

```python
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        ans = []
        
        # Iterate through each word in queries
        for query in queries:
            # Check against every word in the dictionary
            for s in dictionary:
                dis = 0
                # Count mismatches between query and current dictionary word
                for i in range(len(query)):
                    if query[i] != s[i]:
                        dis += 1
                    
                    # Optimization: if distance exceeds 2, this dictionary word fails
                    if dis > 2:
                        break
                
                # If a match is found within 2 edits
                if dis <= 2:
                    ans.append(query)
                    # Move to the next query immediately
                    break
                    
        return ans
```

---

## Example Walkthrough

**Input:** `queries = ["word","note"], dictionary = ["wood","joke","moat"]`

1.  **Query "word":**
    - vs "wood": `w==w, o==o, r!=o, d==d`. Distance = 1. (Match!)
    - Add "word" to `ans`.
2.  **Query "note":**
    - vs "wood": Distance = 3.
    - vs "joke": Distance = 2. (Match!)
    - Add "note" to `ans`.

**Output:** `["word", "note"]`

---

## Complexity Analysis

* **Time Complexity:** $O(Q \times D \times L)$
    - $Q$ is the number of query words.
    - $D$ is the number of dictionary words.
    - $L$ is the length of the strings.
    - In the worst case, we compare every character of every query with every dictionary word.
* **Space Complexity:** $O(1)$ (excluding the output list)
    - We only use a single integer variable `dis` to track character differences.

---

## Tags
String, Array, Enumeration, Brute-Force, Hamming-Distance