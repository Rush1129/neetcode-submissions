class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for n in range(0,len(numbers)):
            comp = target-numbers[n]
            if comp in numbers:
                i1=n+1
                break

        for i in range(0,len(numbers)):
            if comp==numbers[i]:
                i2=i+1
                break

        return [i1,i2]