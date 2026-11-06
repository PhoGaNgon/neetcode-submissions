class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counts = set()

        for n in nums:
            counts.add(n)

        seq = 0
        max_seq = 0
        for n in nums:
            if n - 1 not in counts:
                seq = 1
                while n + 1 in counts:
                    n += 1
                    seq += 1
                if seq > max_seq:
                    max_seq = seq
                    
        return max_seq
