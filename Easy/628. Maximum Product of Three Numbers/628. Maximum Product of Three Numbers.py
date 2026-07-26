class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        (a, b, c), (x, y) = nlargest(3, nums), nsmallest(2, nums)
        return max(a * b * c, a * x * y)