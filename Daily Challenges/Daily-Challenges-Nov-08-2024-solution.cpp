/* # 🟨 LeetCode 1829 - Maximum XOR for Each Query

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1829](https://leetcode.com/problems/maximum-xor-for-each-query/)

# 🧠 Problem Description
# [Github LeetCode 1829 - Maximum XOR for Each Query](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1829.%20Maximum%20XOR%20for%20Each%20Query)
*/

#include <vector>
using namespace std;


class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int mask = (1 << maximumBit) - 1;
        int cumulativeXor = 0;
        vector<int> result(nums.size());
        for (int num : nums) {
            cumulativeXor ^= num ;
        }
        for (int i = 0; i < nums.size(); ++i) {
            result[i] = cumulativeXor ^ mask;
            cumulativeXor ^= nums[nums.size() - 1 - i];
        }
        return result;
    }
};