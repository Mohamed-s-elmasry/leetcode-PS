class Solution(object):
    def pivotIndex(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        for e in range(1, len(nums)):
            nums[e] += nums[e-1]
        if nums[0] == nums[-1]:
            return 0
        for e in range(1, len(nums)):
            if nums[-1] - nums[e] == nums[e-1]:
                return e
        return -1
            