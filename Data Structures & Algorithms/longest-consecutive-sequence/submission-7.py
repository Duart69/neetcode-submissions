class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        max_len = 0
        for num in setNums:
            if num - 1 not in setNums:
                i = 0
                value = num
                while(value in setNums):
                    i+=1
                    value +=1
                if(i > max_len):
                    max_len = i
        return max_len