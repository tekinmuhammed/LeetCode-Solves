class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7
        
        # For row 1
        typeA = 6  # ABA
        typeB = 6  # ABC
        
        for _ in range(2, n + 1):
            newA = (typeA * 3 + typeB * 2) % MOD
            newB = (typeA * 2 + typeB * 2) % MOD
            typeA, typeB = newA, newB
        
        return (typeA + typeB) % MOD