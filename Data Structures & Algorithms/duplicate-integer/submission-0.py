class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use hash set to remove duplicates, if length is less than original then it has duplicates
        return len(set(nums)) < len(nums)
        