class Solution(object):
  def findDisappearedNumbers(self, nums):
    result = []
    for i in range(1, len(nums) + 1):
        result.append(i)
    for num in nums:
        if num in result:
            result.remove(num)
    return result
    