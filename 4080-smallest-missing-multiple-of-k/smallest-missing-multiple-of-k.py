class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        maxm=max(nums)
        nums.sort()
        mtp=[]
        present=[]
        for i in range((maxm//k)+3):
            mtp.append(k+(i*k))
        for j in mtp:
            if j not in nums:
                return j