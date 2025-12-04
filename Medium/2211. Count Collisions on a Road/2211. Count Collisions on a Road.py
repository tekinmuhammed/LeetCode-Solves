class Solution(object):
    def countCollisions(self, directions):
        # Step 1: Leading L cars (en soldaki sola gidenler) asla çarpışmaz → ignore
        i, n = 0, len(directions)
        while i < n and directions[i] == 'L':
            i += 1
        
        # Step 2: Trailing R cars (en sağdaki sağa gidenler) asla çarpışmaz → ignore
        j = n - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1
        
        # Step 3: Ortada kalan bölgede 'S' veya kollisyon yaşayan R ve L arabaları kalır.
        # Burada hareket eden her araba (yani 'R' veya 'L') çarpışmaya sebep olur.
        
        collisions = 0
        for k in range(i, j + 1):
            if directions[k] != 'S':
                collisions += 1
                
        return collisions