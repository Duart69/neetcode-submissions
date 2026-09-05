class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        pre = 1
        for i in range(0,len(nums)):
            result[i] = pre
            pre = pre *nums[i]
        post = nums[len(nums)-1]
        for j in range(len(nums)-2,-1,-1):
            result[j]=result[j]* post
            post = post * nums[j]
        return result