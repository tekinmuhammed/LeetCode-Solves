class Solution(object):
    def totalMoney(self, n):
        total = 0
        current_monday = 1
        
        while n > 0:
            daily = current_monday
            for _ in range(min(7, n)):
                total += daily
                daily += 1
            current_monday += 1
            n -= 7
        
        return total