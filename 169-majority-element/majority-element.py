class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        for num in nums:
            hash[num] = 1 + hash.get(num,0)

            if hash[num] > (len(nums) / 2):
                return num