class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0,len(nums)):
            t = -1*nums[i]
            l=i+1
            r=len(nums)-1

            while l<r:
                if nums[l]+nums[r]==t:
                    tres = [nums[i], nums[l], nums[r]]
                    tres.sort() 
                    if tres not in res:
                        res.append(tres)
                    if l+1<r:
                        if nums[l+1]+nums[r]<=t:
                            l+=1
                        else:
                            r-=1
                    else:
                        break
                elif nums[l]+nums[r]<t:
                    l+=1
                else:
                    r-=1
        return res         