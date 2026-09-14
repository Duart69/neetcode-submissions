class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i,n in enumerate(nums):
            if(i > 0):
                if(n == nums[i-1]):
                    continue
            l = i+1
            r = len(nums)-1
            while(l < r):
                if(l > i+1):
                    if(nums[l]==nums[l-1]):
                        l+=1
                        continue
                if(r < len(nums)-1):
                    if(nums[r] ==nums[r+1]):
                        r-=1
                        continue
                dif = nums[l] + nums[r] + n
                if(dif == 0):
                    res.append([nums[l],nums[r],n])
                    l+=1
                    r-=1
                elif(dif > 0):
                        r-=1
                else:
                        l+=1
        return res
            

