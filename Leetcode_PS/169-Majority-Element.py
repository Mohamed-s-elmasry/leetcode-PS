class Solution(object):
    def majorityElement(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        count = 0
        inti_value =0
        for num in nums :
            if count == 0 :
                inti_value= num 
            count+= (1 if num == inti_value else -1 )
        return inti_value
            


        