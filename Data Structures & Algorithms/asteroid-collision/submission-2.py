class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        for a in asteroids:
            same=False
            if a<0:
                while res:
                    preva=res.pop()
                    if preva<0:
                        res.append(preva)
                        res.append(a)
                        break
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