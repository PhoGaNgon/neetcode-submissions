class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        pref = 1
        suff = 1

        for i in range(length):
            res[i] = pref
            pref *= nums[i]
        for i in range(length - 1, -1, -1):
            res[i] *= suff
            suff *= nums[i]

        return res