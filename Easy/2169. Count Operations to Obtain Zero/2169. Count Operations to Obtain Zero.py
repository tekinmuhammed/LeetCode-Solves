class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # If either is zero already, no operations needed
        if num1 == 0 or num2 == 0:
            return 0

        ops = 0
        a, b = num1, num2

        # Use division to count how many subtractions would happen in bulk
        while a != 0 and b != 0:
            if a >= b:
                ops += a // b       # subtract b from a this many times
                a = a % b           # remainder after those subtractions
            else:
                ops += b // a
                b = b % a

        return ops