from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        answer = []
    
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            freq = Counter(subarray)
        
            most_common = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
        
            x_most_frequent = most_common[:x]
        
            x_sum_value = sum(item[0] * item[1] for item in x_most_frequent)
        
            answer.append(x_sum_value)
        
        return answer
    
        
solution = Solution()
nums = [1, 2, 2, 3, 3, 3]
k = 3
x = 2
print(solution.findXSum(nums, k, x))