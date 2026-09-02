class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if(compl in mapa):
                return [mapa[compl], i]
            mapa[nums[i]]=i