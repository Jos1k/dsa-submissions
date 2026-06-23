class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictL, dictF, output = {}, {}, []

        for n in nums:
            dictL[n] = dictL.get(n, 0) + 1
        
        for key,v in dictL.items():
            dictF.setdefault(v,[]).append(key)

        for i in range(len(nums),0,-1):
            if i in dictF:
                iL = 0
                while len(output) != k and iL < len(dictF[i]):
                    output.append(dictF[i][iL])
                    iL+=1
            
        return output