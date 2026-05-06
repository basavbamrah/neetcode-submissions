class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time= {}
        fleet = 1
        for p,s in zip(position,speed):
            time[p] = ((target-p)/s)
            
        s_pos = sorted(position, reverse=True)
      
        prev_time = time[s_pos[0]]
        for i in s_pos[1:]:
            if  time[i] > prev_time:
                fleet+=1
                prev_time = time[i]
            
        return fleet



