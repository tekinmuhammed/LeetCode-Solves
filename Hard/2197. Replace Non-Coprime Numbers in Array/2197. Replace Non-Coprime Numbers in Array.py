class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        N = len(nums)
        stack = []

        for i in nums:
            stack.append(i)

            while len(stack) >=  2 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                
                l = lcm(a, b)
                stack.append(l)
            
        return stack