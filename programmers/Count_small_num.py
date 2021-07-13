class Solution:
    def countSmaller(self, nums):
        sort_num = sorted(nums)
        counts = []
        for i in nums:
            num_index = sort_num.index(i)
            counts.append(num_index)
            sort_num.remove(i)
        return counts


a = Solution()
print(a.countSmaller([5, 2, 6, 1]))