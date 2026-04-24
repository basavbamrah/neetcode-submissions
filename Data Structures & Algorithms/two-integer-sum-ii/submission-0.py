class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(numbers)-1

        while start<=end:
            mid = (start+end)//2

            target_sum = numbers[start]+numbers[end]
            if target_sum > target:
                end-=1
            elif target_sum < target:
                start +=1
            else:
                return [start+1, end+1]