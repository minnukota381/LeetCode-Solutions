class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        ms=[]
        for i, ch in count.items():
            if ch==2:
                ms.append(i)
        return ms
