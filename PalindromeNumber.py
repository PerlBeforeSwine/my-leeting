class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        
        flipped = 0
        original = x
        
        while x > 0:
            flipped = (flipped * 10) + (x % 10)
            x /= 10
            
        if flipped == original:
            return True
        else:
            return False