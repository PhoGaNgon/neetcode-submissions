class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        stack = []
        water = [0] * n

        for i in range(n):
            if height[i] > 0:
                while stack and height[i] >= height[stack[-1]]:
                    top = stack.pop()
                    water[(top + 1):i] = [min(height[i], height[top])] * (i - top - 1)

                if stack:
                    top = stack[-1]
                    water[(top + 1):i] = [min(height[i], height[top])] * (i - top - 1)
                stack.append(i)

        for i in range(n):
            if water[i] > 0:
                water[i] -= height[i]
                res += water[i]
        
        return res
