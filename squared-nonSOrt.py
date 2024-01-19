"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].
use list comprehension 
"""
def sortedSquares(nums):
    return sorted([i**2 for i in nums])
if __name__ == '__main__':
    nums = list(map(int, input().rstrip().split()))
    result = sortedSquares(nums)
    print(result)