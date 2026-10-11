class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        founded = [False]*128
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1
        l, r = 0,1
        founded[ord(s[l])]=True
        maxLen = 0
        while(r < n):
            asciiChar = ord(s[r])
            if(founded[asciiChar]):
                while(founded[asciiChar]):
                    founded[ord(s[l])]= False
                    l+=1
            founded[asciiChar] = True
            if(r-l+1 > maxLen):
                maxLen = r-l+1
            r+=1
        return maxLen
            

