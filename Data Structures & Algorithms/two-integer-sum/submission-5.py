class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copyNums = [0] * len(nums)
        for index, num in enumerate(nums):
            copyNums[index] = num
        
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            currNum = nums[l] + nums[r]
            if currNum == target:
                idx1 = copyNums.index(nums[l])
                idx2 = copyNums.index(nums[r]) if nums[l] != nums[r] else copyNums.index(nums[r], idx1 + 1)
                return sorted([idx1, idx2])
            elif currNum > target:
                 r -= 1
            else:
                 l += 1
        return []
