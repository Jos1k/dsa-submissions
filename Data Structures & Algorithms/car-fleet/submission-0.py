class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        cars.sort()

        for p,s in cars:
            timeToComplete = (target - p) / s

            while stack and stack[-1] <= timeToComplete:
                stack.pop()

            stack.append(timeToComplete)
        
        return len(stack)