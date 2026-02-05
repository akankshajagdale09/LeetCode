class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Step 1: Keep only alphanumeric characters and convert to lowercase
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        # Step 2: Check if cleaned string is same forwards and backwards
        return cleaned == cleaned[::-1]