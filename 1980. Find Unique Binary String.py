class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums)
        r = []
        
        for i in range(n):
            curr = nums[i][i]
            
            if curr == '0':
                r.append('1')
            else:
                r.append('0')
        
        return ''.join(r)
