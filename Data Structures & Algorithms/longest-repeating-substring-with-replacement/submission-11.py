class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        LettersDict = {}
        l = 0
        maxLen = 0
        for r in range(len(s)):
            LettersDict[s[r]] = LettersDict.get(s[r],0)+1
            while(r-l+1-max(LettersDict.values()) > k):
                LettersDict[s[l]] -= 1
                l+=1
            lenActual = r-l+1
            if lenActual > maxLen: maxLen = lenActual
        return maxLen



            

                
