# Questions to ask 
# what if there are multiple elements ? what if nums is empty whats return then ?
# what if none of the elements qualify wih k freq ?
# nums = [1,2,2,3,3,3] k =2 
# 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreqMap = {}
        for num in nums:
            numToFreqMap[num] = numToFreqMap.get(num, 0) + 1
        res = [[]]
        for key in numToFreqMap:
            res.append([numToFreqMap[key], key])
        res.sort()

        top_k =[]
        for freq, key in res[-k:]:
            top_k.append(key)
        return top_k

        


