class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 1
        max = 1

        if len(nums) == 0:
            return 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                count += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                count = 1
            if count > max:
                max = count

        return max
