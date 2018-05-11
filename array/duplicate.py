class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        index = 0            # the conunt
        for i in nums[0:]:
            if nums[index] != i:
                index += 1
                nums[index] = i
        return index+1

solution = Solution()
nums = [1,1,3,6,6,6,9]
number = solution.removeDuplicates(nums)
print(str(number))