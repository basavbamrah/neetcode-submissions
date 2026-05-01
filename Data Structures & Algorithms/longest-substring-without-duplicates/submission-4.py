class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        if s=="":
            return 0
        sub_s =""
        max_len=1
        for i in range(0,len(s)):
            if s[i] in sub_s:
                start = s.index(s[i], start)+1
                max_len= max(max_len, len(sub_s))
                sub_s=s[start:i]
            sub_s+=s[i]
        return max(max_len, len(sub_s))
