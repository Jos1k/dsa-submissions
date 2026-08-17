class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers)-1
        target_c = numbers[i] + numbers[j]

        while target_c != target:
            if target_c > target: j-=1
            else: i+=1
            target_c = numbers[i] + numbers[j]

        return [i+1,j+1]