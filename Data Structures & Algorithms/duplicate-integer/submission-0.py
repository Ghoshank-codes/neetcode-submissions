class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while nums:
            num=nums.pop(0)
            if num in nums:
                return True
                break
        return False     