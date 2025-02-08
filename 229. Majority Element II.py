class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n=len(nums)//3
        # g=Counter(nums)
        # ls=[]

        # for i,c in g.items():
        #     if c>n:
        #         ls.append(i)
        # return ls
        
        n = len(nums)
        result = []
        
        unique = set(nums)

        for num in unique:
            if nums.count(num) > n // 3:
                result.append(num)
        
        return result
                
