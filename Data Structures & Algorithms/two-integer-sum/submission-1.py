class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sd = dict()
        for i, v in enumerate(nums):
            isThere = sd.get(target - v)
            if isThere is not None:
                return [isThere,i]
            sd[v] = i
        return [] 