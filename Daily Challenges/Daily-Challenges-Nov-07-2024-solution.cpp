/* 🟨 LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2275](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/)

# 🧠 Problem Description
# [Github LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2275.%20Largest%20Combination%20With%20Bitwise%20AND%20Greater%20Than%20Zero)
*/

class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        int maxCount = 0;
        for (int bit = 0; bit < 24; ++bit){
            int count = 0;
            for (int num : candidates) {
                if (num & (1 << bit)) {
                    ++count;
                }
            }
            maxCount = max(maxCount, count);
        }
        return maxCount;
    }

};