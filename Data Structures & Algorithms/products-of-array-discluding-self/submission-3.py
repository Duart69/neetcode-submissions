class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sys.setrecursionlimit(20000)
        result = [0]*len(nums)
        self.productExceptSelf2(nums, 0,1,result)
        return result
    def productExceptSelf2(self, array, index,forward,result):
        if(index == len(array)-1):
            result[index] = forward
            return array[index]
        backward = self.productExceptSelf2(array, index+1, forward*array[index], result)
        result[index]= forward * backward
        return backward*array[index]