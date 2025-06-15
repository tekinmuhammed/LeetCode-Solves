class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common = []
        seen = set()
        count = 0
        for i in range(n):
            if A[i] in seen:
                count += 1
            else:
                seen.add(A[i])
            if B[i] in seen:
                count += 1
            else:
                seen.add(B[i])
            prefix_common.append(count)
        return prefix_common