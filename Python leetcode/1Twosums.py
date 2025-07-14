'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

#bruteForce Approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]==target:
                    return [x,y]
#approach 1 used index()
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            a=target-nums[x]
            if a in nums:
                try:
                    b=nums.index(a,x+1)
                except:
                    pass
                else:
                    return [x,b]
#approach 2 tried without try else block
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            a=target-nums[x]
            if a in nums[x+1:]:
                return [x,nums.index(a,x+1)]
               
#lets BEST ANSER TWO PASS hash map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []
"""create a hash map the index of the elements in array
 get the other number if the number is in hash map and has a diffrent index then those two are your pairs"""

# 1 pass hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []

"""iterating through elements checking if element is already there if it's already there return the index of the previous and 
the current one. Add element to the hash"""

#best usese enumerate()
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for id,value in enumerate(nums):

            diff = target - value
            if diff in seen:
                return [seen[diff], id]
            else:
                seen[value] = id

#Learned about itterables, itterators and generators