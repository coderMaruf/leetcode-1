'''

Description:

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].



Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].



Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

'''



class Solution(object):
    def runningSum(self, nums):
        
        # in-place update running sum in nums
        for idx in range(1, len(nums)):
            
            nums[idx] += nums[idx-1]
            
        return nums



# n : the length of input list, nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index, which is of O( 1 ).


import unittest
class Testing(unittest.TestCase):

    def test_case_1(self):

        result = Solution().runningSum( nums = [1,2,3,4] )
        self.assertEqual( result,  [1,3,6,10] )


    def test_case_2(self):

        result = Solution().runningSum( nums = [1,1,1,1,1] )
        self.assertEqual( result,  [1,2,3,4,5] )


    def test_case_3(self):
    
        result = Solution().runningSum( nums = [3,1,2,10,1] )
        self.assertEqual( result,  [3,4,6,16,17] )


if __name__ == '__main__':

    unittest.main()