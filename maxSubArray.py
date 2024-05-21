"""
Given an integer array nums, find the subarray with the largest sum,
and return its sum.

"""

# Kadane's Algorithm
def max_subarray(nums: list) -> int:
    max_current = max_global = nums[0]

    for idx in range(1, len(nums)):
        # Update max_current to include the current element
        max_current = max(nums[idx], max_current + nums[idx])
        # Update max_global to be the maximum of max_global and max_current
        if max_current > max_global:
            max_global = max_current

    return max_global

# Example usage
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))  # Output: 6 (subarray [4,-1,2,1])

nums = [1]
print(max_subarray(nums))  # Output: 1 (subarray [1])

nums = [5,4,-1,7,8]
print(max_subarray(nums))  # Output: 23 (subarray [5,4,-1,7,8])

nums = [-1, -2, -3, -4]
print(max_subarray(nums))  # Output: -1 (subarray [-1])




