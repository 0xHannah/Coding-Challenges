class Solution:
    def runningSum(self, nums):
        x = nums
        y = 0
        z = 0
        for num in nums:
            z += 1
            x[z-1] += y
            y += num
        return x