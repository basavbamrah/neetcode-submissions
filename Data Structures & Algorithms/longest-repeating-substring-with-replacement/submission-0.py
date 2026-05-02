class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        start =0
        max_f = 0
        max_l =0
        for i in range(len(s)):
            c[s[i]]= c.get(s[i], 0)+1

            max_f= max(max_f, c[s[i]])

            while (i-start +1) - max_f >k:
                c[s[start]]-=1
                start+=1
            
            max_l = max(max_l, i-start+1)

        return max_l