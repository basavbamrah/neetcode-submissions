class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        count = 0
        for i in num_set:

            if i-1 not in num_set:
                curr = i
                c = 1

                while curr+1 in num_set:
                    curr+=1
                    c+=1
                count = max(count, c)

        return count
            