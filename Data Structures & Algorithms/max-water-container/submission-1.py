class Solution:
    def maxArea(self, arr: List[int]) -> int:
        
        s, e = 0, len(arr)-1
        cap = min(arr[s], arr[e])* (e-s) 
        while s<e:
            c = min(arr[s], arr[e])* (e-s)

            if c>cap:
                cap=c

            if arr[s]<arr[e]:
                s+=1
            else:
                e-=1
        
        return cap

