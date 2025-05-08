class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        result = []
        
        for word in words:
            if len(word) <= 2:
                result.append(word.lower())
            else:
                result.append(word.capitalize())
        
        return " ".join(result)
