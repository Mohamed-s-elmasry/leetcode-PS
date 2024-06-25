class Solution(object):
    def lengthOfLastWord(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        res = s.split()
        counter = 0
        for i in range(len(res[-1])):
            counter+=1
        return counter
        