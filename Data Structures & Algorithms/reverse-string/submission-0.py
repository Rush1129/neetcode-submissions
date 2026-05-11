class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        string = ''

        for i in s:
            string+= i
        
        for i in range(0,len(string)):
            s[len(s)-1-i] = string[i]