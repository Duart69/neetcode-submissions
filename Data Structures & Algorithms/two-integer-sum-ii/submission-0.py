class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while(l<r):
            sumRes = numbers[l] + numbers[r]
            if(sumRes == target):
                return [l+1,r+1]
            if(sumRes > target):
                r-=1
            else:
                l+=1
        return -1
        