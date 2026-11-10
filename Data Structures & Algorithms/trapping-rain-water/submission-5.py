class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pref = [0] * n
        suff = [0] * n
        water = [0] * n
        m = 0
        res = 0

        for i in range(n):
            m = max(m, height[i])
            pref[i] = m

        m = 0
        for i in range(n - 1, -1, -1):
            m = max(m, height[i])
            suff[i] = m

        for i in range(n):
            water[i] = min(pref[i], suff[i])

        for i in range(n):
            res += water[i] - height[i]
        
        return res
