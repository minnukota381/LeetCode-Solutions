class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        s_list = list(s)

        vowel_list = []
        for char in s_list:
            if char in vowels:
                vowel_list.append(char)

        vowel_list.reverse()

        result = []
        vowel_index = 0
        for char in s_list:
            if char in vowels:
                result.append(vowel_list[vowel_index])
                vowel_index += 1
            else:
                result.append(char)

        return "".join(result)
