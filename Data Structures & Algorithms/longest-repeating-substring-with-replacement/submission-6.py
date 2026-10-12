class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countLetters = [0]*26
        n = len(s)
        if(n==1):return 1
        l,r= 0,1
        letter = s[l]
        countLetters[ord(s[l])-65]+=1
        distinct = 0
        maxLen = 0
        while(r<n):
            countLetters[ord(s[r])-65] += 1
            if(not s[r] == letter):
                distinct += 1
            if(countLetters[ord(s[r])-65] > countLetters[ord(letter)-65]):
                distinct = distinct + countLetters[ord(letter)-65] - countLetters[ord(s[r])-65]
                letter = s[r]
            if(distinct > k):
                while(distinct>k):
                    countLetters[ord(s[l])-65]-=1
                    if(not s[l] == letter):
                        distinct -=1
                    l+=1
                    letterMax = countLetters.index(max(countLetters))
                    if(countLetters[letterMax] > countLetters[ord(letter)-65]):
                        distinct = distinct + countLetters[ord(letter)-65] - countLetters[letterMax]
                        letter = chr(letterMax+65)
            if(r-l+1>maxLen):
                maxLen = r-l+1
            r+=1
        return maxLen
            

                
