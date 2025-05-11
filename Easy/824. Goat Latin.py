class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        words = sentence.split()
        result = []

        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
            goat_word += 'a' * (i + 1)
            result.append(goat_word)

        return ' '.join(result)
        