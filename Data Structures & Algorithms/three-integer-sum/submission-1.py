class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        setList = set()
        nums = sorted(nums)
        for i,n in enumerate(nums):
            l = i+1
            r = len(nums)-1
            while(l < r):
                dif = nums[l] + nums[r]
                if(dif == -n):
                    lis = [nums[l],nums[r],n]
                    lis = tuple(sorted(lis))
                    if(not(lis in setList)):
                        res.append(lis)
                        setList.add(lis)
                    l+=1
                    r-=1
                else:
                    if(dif > -n):
                        r-=1
                    else:
                        l+=1
        return res
            

