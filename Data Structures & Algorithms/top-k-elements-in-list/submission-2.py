class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        counts = {}
        res = []

        for num in nums: # key = num, val = count
            counts[num] = counts.get(num, 0) + 1
        for key in counts:
            freq[counts[key]].append(key)
        for i in reversed(freq):
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res
