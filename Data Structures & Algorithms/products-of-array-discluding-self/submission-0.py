class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        pref,suf = [1]*n,[1]*n
        p,s = 1,1
        for i in range(1,n):
            p *= nums[i-1]
            pref[i] = p

        for i in range(n-2,-1,-1):
            s *= nums[i+1]
            suf[i] = s

        pro = [0]*n
        for i in range(n):
            pro[i] = pref[i]*suf[i]

        return pro 