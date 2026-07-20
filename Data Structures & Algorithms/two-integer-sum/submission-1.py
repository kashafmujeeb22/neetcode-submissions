# [3,4,5,6] , target = 7 
#  SORT, will the array always be sorted ?
# [3,4,5,6]
# Time complexity = O(n), Space complexity = O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, number in enumerate(nums):
            indices[number] = index
        for index, number in enumerate(nums):
            difference = target - number
            if difference in indices and indices[difference] != index:
                return [index, indices[difference]]
        return []
