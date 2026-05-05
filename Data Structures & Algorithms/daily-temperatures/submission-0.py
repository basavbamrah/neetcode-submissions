class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results=[0]*len(temperatures)
        start, end = 0, 1
        while start<len(temperatures):
            if start == len(temperatures)-1:
                break
            elif temperatures[end]>temperatures[start]:
                print(start,end)
                results[start]= end-start
                start+=1
                end=start
            
            end+=1
            if end == len(temperatures):
                # results[start]=0
                start+=1
                end = start+1
        
        return results