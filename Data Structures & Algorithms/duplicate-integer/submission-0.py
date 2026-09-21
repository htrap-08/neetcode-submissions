class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set(nums)
        a = True
        if len(num) == len(nums):
            a = False
        return a