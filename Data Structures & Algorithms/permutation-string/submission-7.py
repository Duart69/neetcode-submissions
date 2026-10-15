class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = {}
        for c in s1:
            letters[c] = letters.get(c, 0)+1
        l = 0
        aux = letters.copy()
        for r in range(len(s2)):
            if(s2[r] in aux):
                aux[s2[r]] -= 1
                if(aux[s2[r]] == 0):
                    del aux[s2[r]]
                    if(not aux):
                        return True
            else:
                aux = letters.copy()
                if(s2[r] in letters):
                    l = r
                    while(l > 0 and s2[l] in aux):
                        aux[s2[l]]-=1
                        if(aux[s2[l]] == 0):
                            del aux[s2[l]]
                        if(not aux):
                            return True
                        l-=1
                    l+=1
                else:
                    l = r+1
        return False
        