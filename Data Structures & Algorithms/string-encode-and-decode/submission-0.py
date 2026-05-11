class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ''
        for s in strs:
            for ss in s:
                en+=str(ord(ss))
                en+=' '
            en+='\n'

        return en 

    def decode(self, s: str) -> List[str]:
        de = []
        temp = ''
        strs = ''
        i = 0
        while(i<len(s)):
            if(s[i] == '\n'):
                de.append(temp)
                temp = ''
                i+=1
                continue
            nxt = i+1
            strs = s[i]
            while(s[nxt] != ' '):
                strs+=s[nxt]
                nxt+=1
            i = nxt + 1
            temp+=(chr(int(strs)))

        return de

