class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # r=[]
        # for i in range(len(nums)):
        #     r.append(nums[i]**2)

        # r.sort()
        # return r
        
        return sorted(map(lambda x: x * x, nums))


        