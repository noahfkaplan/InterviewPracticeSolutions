class Solution:
  def sortColors(self, nums):
    colorCounts = [0, 0, 0]
    for color in nums:
        colorCounts[color] += 1
    nums.clear()
    nums.extend([0] * colorCounts[0] + [1] * colorCounts[1] + [2] * colorCounts[2])