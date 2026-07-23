class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if(len(nums)<=1):
            return nums

        mid = len(nums)//2
        lms = self.sortArray(nums[:mid])
        rms = self.sortArray(nums[mid:])
        return self.mergeArray(lms,rms)
        
    def mergeArray(self,lms,rms):
        res = []
        i,j = 0,0

        while(i<len(lms) and j<len(rms)):
            if(lms[i]<rms[j]):
                res.append(lms[i])
                i+=1
            else:
                res.append(rms[j])
                j+=1
        
        res.extend(lms[i:])
        res.extend(rms[j:])

        return res
        