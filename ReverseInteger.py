class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # check for an easy return value
        if x == 0:
            return 0
        # optionally check if the input is larger than a signed integer should be
        elif x > ((2**31)-1) or x < (0 - (2**31)):
            return 0
        
        # storage for our reversed number
        flipped = 0
        
        #retain pos/neg values:
        negFlag = 1
        
        if x < 0:
            negFlag = -1
            x *= -1
        
        while x > 0:
            flipped = (flipped * 10) + (x % 10)
            x = x / 10
            
        if flipped > (2**31-1) or flipped < (0 - (2**31)):
            return 0
        else:
        # return our reversed value, with negative flag as needed
            return (flipped * negFlag)