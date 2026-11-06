class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length
        pref = [0] * length
        suff = [0] * length

        pref[0] = 1
        suff[length - 1] = 1

        for i in range(1, length):
            pref[i] = (pref[i - 1] * nums[i - 1])
        for i in range(length - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]

        for i in range(length):
            res[i] = pref[i] * suff[i]

        return res