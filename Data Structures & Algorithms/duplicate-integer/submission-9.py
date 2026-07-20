#Hash set length approach
#[1,2,2,3,4,5]
# set length < nums length = True
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))    