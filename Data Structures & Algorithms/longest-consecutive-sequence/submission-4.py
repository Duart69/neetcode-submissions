class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        minheap = nums
        heapq.heapify(minheap)
        if(len(minheap) > 0):
            prev = heapq.heappop(minheap)
            i = 1
            max_len = 1
            while(len(minheap) > 0):
                value = heapq.heappop(minheap)
                if(value == (prev+1)):
                    i+=1
                elif(value != prev):
                    if(i > max_len):
                        max_len = i
                    i = 1
                prev = value
            return max(max_len, i)
        else:
            return 0
