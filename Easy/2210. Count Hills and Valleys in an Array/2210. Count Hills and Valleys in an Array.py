class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        j=0 #to point towards the valid left element to be compared
        for i in range(1,n-1):
            if (nums[i]>nums[i+1] and nums[i]>nums[j]) or (nums[i]<nums[i+1] and nums[i]<nums[j]):
                ans+=1
                j=i
        return ans