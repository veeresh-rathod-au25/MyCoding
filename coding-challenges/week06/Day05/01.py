class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        
        i = j = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):

                if nums1[i] == nums2[j]:
                    l.append(nums1[i])

                elif nums1[i] > nums2[j]: j += 1
                else: i += 1
        return l


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        m=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if(nums1[i]==nums2[j]):
                    m.append(nums1[i])
        return set(m)