class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sd = dict()
        val = []
        for i, v in enumerate(nums):
            isThere = sd.get(target - v)
            if isThere is not None:
                val.extend([isThere, i])
                break
            sd[v] = i
        return val 