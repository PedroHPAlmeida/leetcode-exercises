from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            for index2, num2 in enumerate(nums[index + 1:]):
                if num + num2 == target:
                    return [index, index + index2 + 1]
