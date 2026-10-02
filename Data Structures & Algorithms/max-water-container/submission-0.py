class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ini = 0
        fi = len(heights)-1
        maxArea = (fi-ini)*min(heights[ini], heights[fi])
        while(ini < fi):
            if(heights[ini]<heights[fi]):
                value = heights[ini]
                while((heights[ini] <= value)and (ini < fi)):
                    ini +=1
            elif(heights[ini] == heights[fi]):
                ini+=1
                fi-=1
            else:
                value = heights[fi]
                while((heights[fi] <= value)and (ini < fi)):
                    fi -=1 
            if(ini < fi):
                area = (fi-ini)*min(heights[ini], heights[fi])
                if(area > maxArea):
                    maxArea = area
        return maxArea
                
