class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # counter for first number's index
        i = 0
        
        
        for i in range (0,len(nums)):
            # for each number, see if there's a later number on the list that adds up to target
            if (target-nums[i]) in nums[i+1:]:
                # when found, return the first number's index and
                # find the second number's index in the remainder of the list
                # + i + 1 at the end is to return us to the original list's index values
                return [i,nums[i+1:].index(target-nums[i])+i+1]
            
        return "no solution"