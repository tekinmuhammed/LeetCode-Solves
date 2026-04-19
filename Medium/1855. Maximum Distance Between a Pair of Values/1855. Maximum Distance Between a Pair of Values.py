class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        mat=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                mat=max(mat,abs(j-i))
                j+=1
            else:
                i+=1
            if j<i:
                j=i
        return mat