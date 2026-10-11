class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1
        l, r = 0,1
        founded = {s[l]}
        maxLen = 0
        while(r < n):
            while(s[r] in founded):
                founded.remove(s[l])
                l+=1
            founded.add(s[r])
            if(r-l+1 > maxLen):
                maxLen = r-l+1
            r+=1
        return maxLen
            

