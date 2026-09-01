class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        letters = [0]*26
        for i in range(len(s)):
            elemS = s[i]
            elemT = t[i]
            letters[ord(elemS)-97] += 1
            letters[ord(elemT)-97] -= 1
        if(min(letters) != 0 or max(letters) != 0):
            return False
        return True