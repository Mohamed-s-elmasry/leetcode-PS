class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter =0 
        for  i in range(len(nums)):
            if nums[i] != val :
                nums[counter] = nums[i]
                counter +=1
            
        return counter
