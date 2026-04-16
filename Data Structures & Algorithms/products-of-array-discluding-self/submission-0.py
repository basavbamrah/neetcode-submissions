class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(len(nums)):
            sum_=1
            # print(sum_)
            for j in range(len(nums)):
                if i==j:
                    continue
                    
                sum_ *=nums[j]
                
            lst.append(sum_)
        
        return lst