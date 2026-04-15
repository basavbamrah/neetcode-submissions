class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = dict()

        for i in strs:
            k = "".join(sorted(i))
            ana_dict[k]= ana_dict.get(k, []) + [i]
        
        return [v for v in ana_dict.values()]
