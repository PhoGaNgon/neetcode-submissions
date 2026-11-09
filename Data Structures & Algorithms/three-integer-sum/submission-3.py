class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    triplet = sorted([nums[i], nums[l], nums[r]])
                    if triplet not in res:
                        res.append(triplet)
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    l += 1

        return res
                
