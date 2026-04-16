class Solution:

    def encode(self, strs: List[str]) -> str:
        l = len(strs)
        if l==0:
            return "None"
        if l==1 and strs[0]=="":
            return ""
        enc_str="@ # $".join(strs)
        return enc_str

    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return [""]
        if s is "None":
            return []
        return s.split("@ # $")