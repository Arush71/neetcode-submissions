class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr=[0]*(len(nums)*2)
        j = 0
        for i in range(len(nums)):
            arr[i]=nums[i]
        j = len(nums)
        for i in range(len(nums)):
            arr[j]=nums[i]
            j+=1
        return arr 