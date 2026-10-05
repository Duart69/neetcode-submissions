class Solution:
    def trap(self, height: List[int]) -> int:
        ini = 0
        fi = len(height)-1
        count = 0
        while(ini < fi):
            if(height[ini] <= height[fi]):
                value = height[ini]
                ini += 1
                while(height[ini] < height[fi] and ini < fi):
                    if(height[ini] > value):
                        value = height[ini]
                    else:
                        count += (value-height[ini])
                    ini+=1
            else:
                value = height[fi]
                fi -= 1
                while(height[fi] < height[ini] and ini < fi):
                    if(height[fi] > value):
                        value = height[fi]
                    else:
                        count += (value - height[fi])
                    fi-=1
        return count

        