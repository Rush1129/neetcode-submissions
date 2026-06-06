class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        ans.append(max(nums[:k]))
        for i in range(1,len(nums)-k+1):
            cur=nums[i:i+k]
            
            
            if cur[k-1]>=ans[-1]:
                ans.append(cur[k-1])
            else:
                tmax=-9999
                for j in range(k):
                    tmax= max(tmax,cur[j])
                ans.append(tmax)
        return ans