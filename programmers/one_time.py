class Solution:
    def singleNumber(self, nums):
        nums_set = set(nums)
        for i in nums_set:
            print(i)
        print(nums_set)
        return nums


a = Solution()
a.singleNumber([1,2,1,3,2,5])