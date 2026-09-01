class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setDup = set()
        for i in range(len(nums)):
            elem = nums[i]
            if elem in setDup:
                return True
            setDup.add(elem)
        return False