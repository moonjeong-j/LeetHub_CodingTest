class Solution:
    def twoSum(self, nums, target) :
        
        nums_i = {nums[i]:i for i in range(len(nums))}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_i.keys():
                if i != nums_i[diff]:
                    return [i, nums_i[diff]]
                
        