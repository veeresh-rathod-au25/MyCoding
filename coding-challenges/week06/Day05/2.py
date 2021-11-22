class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return nums1
        for i in range(n):
            nums1[i+m] = nums2[i]
        return nums1.sort()


                
