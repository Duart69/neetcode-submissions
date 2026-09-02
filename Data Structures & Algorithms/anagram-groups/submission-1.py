class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mapPos = {}
        i = -1
        for s in strs:
            st = "".join(sorted(s))
            if(st in mapPos):
                result[mapPos.get(st)].append(s)
            else:
                i+=1
                mapPos[st] = i
                result.append([s])
        return result