class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        count = 0

        while(l < r):
            if(maxL <= maxR):
                l += 1
                maxL = height[l] if maxL < height[l] else maxL
                count += maxL - height[l]
            else:
                r -= 1
                maxR = height[r] if maxR < height[r] else maxR
                count += maxR - height[r]
        return count

        