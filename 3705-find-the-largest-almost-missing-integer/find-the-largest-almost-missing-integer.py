class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        m=n-k
        missing={x:0 for x in nums}
        for i in range(m+1):
            seen=set()
            for j in range(k):
                g=i+j
                if nums[g] not in seen:
                    missing[nums[g]]+=1
                    seen.add(nums[g])
        for key in sorted(missing, reverse=True):
            if missing[key]==1:
                return key
        return -1