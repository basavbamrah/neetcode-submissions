class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict=dict()
        for i in nums:
            count_dict[i] = count_dict.get(i,0)+1
        
        bucket = [[] for i in range(len(nums)+1)]

        for key,v in count_dict.items():
            bucket[v].append(key)
        lst =[]
        for i in range(len(bucket)-1 , 0, -1):
            for j in bucket[i]:
                lst.append(j)
                if len(lst)==k:
                    return lst
