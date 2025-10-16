# 966. Vowel Spellchecker

# **Difficulty:** Medium  
# **Link:** [LeetCode 966](https://leetcode.com/problems/vowel-spellchecker/)

# 🧠 Problem Description 
# [Github LeetCode 966. Vowel Spellchecker](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/966.%20Vowel%20Spellchecker)

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        vowels = set("aeiou")

        def devowel(word):
            return "".join('*' if ch in vowels else ch for ch in word.lower())

        # 1. Doğrudan eşleşmeler için set
        words_perfect = set(wordlist)

        # 2. Case-insensitive eşleşmeler
        words_case = {}
        for w in wordlist:
            lw = w.lower()
            if lw not in words_case:
                words_case[lw] = w

        # 3. Vowel-hatası eşleşmeleri
        words_vowel = {}
        for w in wordlist:
            vw = devowel(w)
            if vw not in words_vowel:
                words_vowel[vw] = w

        ans = []
        for q in queries:
            if q in words_perfect:
                ans.append(q)  # Case-sensitive tam eşleşme
            elif q.lower() in words_case:
                ans.append(words_case[q.lower()])  # Case-insensitive
            elif devowel(q) in words_vowel:
                ans.append(words_vowel[devowel(q)])  # Vowel-error
            else:
                ans.append("")  # Hiç eşleşme yok
        return ans