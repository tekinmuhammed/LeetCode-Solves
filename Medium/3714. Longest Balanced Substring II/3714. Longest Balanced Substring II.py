class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
    # Iterate through masks 1 to 7 (binary 001 to 111)
        for mask in range(1, 8):
        # Map stores state -> first_index
        # State is a tuple of relative differences
            idx_map = {tuple([0] * (bin(mask).count('1') - 1)): -1}
            counts = [0, 0, 0] # counts for a, b, c
        
            start_index = 0
            for i, char in enumerate(s):
                val = ord(char) - ord('a')
            
            # If current char is NOT in our mask
                if not ((mask >> val) & 1):
                # Reset everything, treat this as a "wall"
                    counts = [0, 0, 0]
                # Reset map: Key is tuple of 0s based on mask size
                    idx_map = {tuple([0] * (bin(mask).count('1') - 1)): i}
                    start_index = i + 1
                    continue
            
                counts[val] += 1
            
            # Build state: differences relative to the first active char in mask
                state = []
                active_counts = [counts[j] for j in range(3) if (mask >> j) & 1]
            
                if active_counts:
                    base = active_counts[0]
                    for k in range(1, len(active_counts)):
                        state.append(active_counts[k] - base)
            
                current_state = tuple(state)
            
                if current_state in idx_map:
                    res = max(res, i - idx_map[current_state])
                else:
                    idx_map[current_state] = i
        return res