class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        chars=dict()
        for i in s:
            if i not in chars:
                chars[i]=1
            else:
                chars[i]+=1
        
        for i in t:
            if i not in chars.keys():
                return False
            if chars[i] == 0:
                return False
            chars[i]-=1
        
        return True
        
        