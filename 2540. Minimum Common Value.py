class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1 = set(nums1)
        s2 = set(nums2)

        s3 = s1.intersection(s2)
        r = list(s3)
        r.sort()
        
        if r:
            return r[0]
        else:
            return -1 
