class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict=dict()
        for i in nums:
            count_dict[i] = count_dict.get(i,0)+1
        
        top_k_freq = sorted(list(count_dict.values()), reverse= True)[:k]
        lst =[]
        for k,v in count_dict.items():
            if v in top_k_freq:
                lst.append(k)
        
        return lst 