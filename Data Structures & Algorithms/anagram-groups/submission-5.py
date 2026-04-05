class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        chars = {}

        for c in s:
            chars[c] = chars.get(c, 0) + 1

        for c in t:
            if c not in chars or chars[c] == 0:
                return False
            chars[c] -= 1

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        final=[]
        seen=[]
        for i in range(len(strs)):
            if strs[i] in seen:
                continue
            ana =[]
            ana.append(strs[i])
            
            for j in strs[i+1:]:
                if self.isAnagram(strs[i],j):
                    ana.append(j)
                    seen.append(j)
            final.append(ana)
        
        return final
