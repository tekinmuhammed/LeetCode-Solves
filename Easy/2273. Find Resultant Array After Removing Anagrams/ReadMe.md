# 🧩 2273. Find Resultant Array After Removing Anagrams
**Difficulty:** Easy  
**Problem Link:** [LeetCode 2273](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/)

---

## 💬 Problem Description  
You are given a list of words. You must remove all words that are **anagrams** of the previous word in the list — meaning that after sorting their characters, they become identical.  

Return the resultant list after removing these consecutive anagrams.

---

## 💡 Intuition  
The main idea is to **compare each word with the last kept word** (not just the previous one in the original array).  
If two consecutive words are anagrams (i.e., their sorted characters match), we skip adding the current word.  
Otherwise, we append it to the result list.

This approach works because sorting the characters of two anagrams will produce the same string.

---

## 🧠 Example  
```python
Input: words = ["abba", "baba", "bbaa", "cd", "cd"]
Output: ["abba", "cd"]
```

### Explanation:

- "baba" and "bbaa" are anagrams of "abba", so they are removed.

- The next word "cd" is not an anagram, so it's kept.

- The final "cd" is identical to the last word, so it’s removed.

## 🧰 Code Implementation
```python
class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = [words[0]]
        
        for i in range(1, len(words)):
            # Eğer mevcut kelime öncekiyle anagram değilse ekle
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])
        
        return result
```

### 📊 Complexity Analysis

- **Time Complexity:**	`O(n * k log k)` — where `n` is the number of words and `k` is the average word length (for sorting each word).

- **Space Complexity:**	`O(k)` — for temporary storage while sorting words.

### 🧷 Tags
`Array` · `String` · `Sorting` · `Anagram` · `Simulation`