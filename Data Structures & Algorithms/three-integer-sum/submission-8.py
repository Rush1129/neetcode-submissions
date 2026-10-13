class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans=[]
        for l in range(0,len(nums)):
            r=len(nums)-1
            t=l+1
            while(t<r):
                three_sum = nums[l]+nums[t]+nums[r]
                three_sum_l = [nums[l],nums[t],nums[r]]
                if three_sum<0:
                    t+=1
                elif three_sum>0:
                    r-=1    
                elif three_sum==0 and three_sum_l not in ans:
                    ans.append(three_sum_l)
                    t+=1
                else:
                    t+=1
        
        return ans