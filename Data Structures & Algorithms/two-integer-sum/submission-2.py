class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sd = dict()
        for i, v in enumerate(nums):
            com=target-v
            if com in sd:
                return [sd[com],i]
            sd[v] = i
        return [] 