class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        target=k
        while target in nums:
            target+=k
        return target