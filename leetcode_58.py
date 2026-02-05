class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading/trailing spaces
        s = s.strip()
        
        # Split the string into words
        words = s.split()
        
        # Return length of the last word
        return len(words[-1])