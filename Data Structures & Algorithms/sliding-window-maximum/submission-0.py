class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxQueue = deque()
        output = []
        l = 0

        for r in range(len(nums)):
            if maxQueue and l > maxQueue[0][1]:
                maxQueue.popleft()

            while maxQueue and maxQueue[-1][0] < nums[r]:
                maxQueue.pop()
            maxQueue.append((nums[r], r))

            if r + 1 - l == k:
                output.append(maxQueue[0][0])
                l+=1
        
        return output
            

        