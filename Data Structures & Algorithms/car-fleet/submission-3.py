class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = zip(position,speed)
        sorted_pair = sorted(zipped, reverse=True) 
        stack=[]
    
        for p,s in sorted_pair:
            time = (target-p)/s
            
            if stack and time<=stack[-1]:
                continue

            stack.append(time)
            
        return len(stack)
