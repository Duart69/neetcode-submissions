class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        for i in range(1,len(nums)):
            result[i] = result[i-1]*nums[i-1]
        aux = [nums[len(nums)-1]]*len(nums)
        for j in range(len(nums)-2,-1,-1):
            result[j]=result[j]* aux[j+1]
            aux[j] = aux[j+1]*nums[j]
        return result