class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        return (int)(l*(l+1)/2 - sum(nums))

a= Solution()
print(a.missingNumber([1,0,3]))