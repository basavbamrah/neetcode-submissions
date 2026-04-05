class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup=dict()
        for i in nums:
            if i in dup.keys():
                return True
            dup[i]=1
        return False