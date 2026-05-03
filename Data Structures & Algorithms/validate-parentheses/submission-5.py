class Solution:
    def isValid(self, s: str) -> bool:
        lst =[]
        val_pair={
            '}':"{",
            "]":"[",
            ")":"("
        }
        if len(s)<2:
            return False
        for i in s:
            if i in "({[":
                lst.append(i)
            elif  len(lst) > 0 and lst[-1] == val_pair[i]:
                lst.pop()
            else:
                return False 
        
        if len(lst) > 0:
            return False
        return True