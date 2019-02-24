#Maximum sub array

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#  https://leetcode.com/problems/maximum-subarray/

def maxSubArray( nums):
    global_max = nums[0]
    current_max = nums[0]
    local_start = 0
    start = 0
    end = 0

    for i in range(1,len(nums)):
        if (current_max + nums[i]) < nums[i]:
            current_max = nums[i]
            local_start = nums[i]
        else:
            current_max = current_max + nums[i]
        if current_max > global_max:
            global_max = current_max
            end = nums[i]
            start = local_start

    print (start,end)
    return global_max



if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(maxSubArray([-10,-1,-2,-3,-4,-5,-6]))

