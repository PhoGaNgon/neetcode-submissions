class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total_product = 1
        num_zeros = 0

        for n in nums:
            if n == 0:
                num_zeros = num_zeros + 1
            else:
                total_product = total_product * n

        if num_zeros > 1:
            return [0] * len(nums)

        for n in nums:
            if num_zeros > 0 and n != 0:
                res.append(0)
            elif n == 0:
                res.append(total_product)
            else:
                res.append(int(total_product / n))
        
        return res