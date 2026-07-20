#Hashmap once pass solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexValMap = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in indexValMap:
                return [indexValMap[diff], index]
            indexValMap[number] = index
        return []    