class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        for a in asteroids:
            same=False
            if a<0:
                while res:
                    if res[-1]<0:
                        res.append(a)
                        break
                    preva=res.pop()
                    if -preva==a: 
                        same=True
                        break
                    if -preva<a: 
                        res.append(preva)
                        break
                if not res and not same: res.append(a)
            else:
                res.append(a)

        return res 