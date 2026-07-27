class Solution:
   def hasDuplicate(self, nums: List[int]) -> bool:
    newlist=set()
    for num in nums:
        newlist.add(num)


    if len(nums)== len(newlist):
      return False
    else:
      return True
        