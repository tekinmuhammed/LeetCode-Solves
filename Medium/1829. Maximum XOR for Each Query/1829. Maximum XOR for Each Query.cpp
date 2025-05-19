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