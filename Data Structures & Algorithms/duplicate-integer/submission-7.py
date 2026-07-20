#sort the array
#run 2 pointers if they are same elements you got a duplicate
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for x in range(1, len(nums)):
            if(nums[x] == nums[x-1]):
                return True
        return False    