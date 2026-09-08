class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr=[0]*(len(nums)*2)
        j = 0
        for i in range(len(nums)*2):
            if i>len(nums)-1:
               arr[i] = nums[j]
               j+=1
               continue
            arr[i]=nums[i]
        return arr 