# 3201. Find the Maximum Length of Valid Subsequence I

# **Difficulty:** Easy  
# **Link:** [LeetCode 3201](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i)

# 🧠 Problem Description 
# [Github LeetCode 3201. Find the Maximum Length of Valid Subsequence I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3201.%20Find%20the%20Maximum%20Length%20of%20Valid%20Subsequence%20I)

class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        mx = 0
        cnt = 0
        for e in nums:
            if e % 2 == 0:
                cnt += 1
            else:
                continue
        
        mx = max(mx, cnt)

        cnt = 0
        for e in nums:
            if e % 2 == 1:
                cnt += 1
            else:
                continue
        
        mx = max(mx, cnt)

        print(mx)

        flag = True

        cnt = 0
        for e in nums:
            if flag:
                if e % 2 == 1:
                    cnt += 1
                    flag = False
                else:
                    continue
            else:
                if e % 2 == 0:
                    cnt += 1
                    flag = True
                else:
                    continue
        
        mx = max(mx, cnt)
        
        flag = False

        cnt = 0
        for e in nums:
            if flag:
                if e % 2 == 1:
                    cnt += 1
                    flag = False
                else:
                    continue
            else:
                if e % 2 == 0:
                    cnt += 1
                    flag = True
                else:
                    continue
        
        mx = max(mx, cnt)

        return (mx)