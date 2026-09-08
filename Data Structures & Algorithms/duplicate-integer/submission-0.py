class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hax=set()
        for n in nums:
            if n in hax:
                return True
            hax.add(n)
        return False
        