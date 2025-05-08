class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        c1 = Counter(nums1)
        c2 = Counter(nums2)

        r = []

        for n in c1 :
            if n in c2:
                t = min(c1[n],c2[n])
                r.extend([n]*t)
        return r