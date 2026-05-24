class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d={}
        for i in range(len(position)):
            d[position[i]]=speed[i]
        
        position.sort(reverse=True)
        
        timel=[]

        for i in position:
            timel.append((target-i)/d[i])
        
        print(timel)
        stack=[]
        fleet=0
        for i in timel:
            if stack==[]:
                stack.append(i)
            elif i<=stack[-1]:
                continue
            else:
                stack.append(i)
                fleet+=1

        return fleet+1
