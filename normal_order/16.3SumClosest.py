'''

16. 3Sum Closest

Medium

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


'''

test_case = [-1, 2, 1, -4]
target = 1

class Solution:	
# Runtime: 44 ms, faster than 99.27% of Python3 online submissions for 3Sum Closest.

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # print(nums)
        output = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # make it faster, runtime will be 96ms without this part
            minsum = nums[i] + nums[i+1] + nums[i+2]
            maxsum = nums[i] + nums[-1] + nums[-2]
            if (minsum > target):
                if (abs(minsum - target) < abs(output - target)):
                    output = minsum
                return output
            if (maxsum < target):
                if (abs(maxsum - target) < abs(output - target)):
                    output = maxsum
                continue

            # 2 ptrs begins    
            l, r = i+1, len(nums)-1
            while l < r:

                tmp = nums[i] + nums[l] + nums[r]
                dis = abs(target - tmp)
                                   
                if tmp < target:
                    l += 1
                elif tmp > target:
                    r -= 1
                else:
                    return target

                closest = tmp

                if (dis < abs(target - output)):
                    # print(i, l, r, 'dis:', dis, 'dis_pre:', dis_pre)
                    output = closest
        return output

print(Solution.threeSumClosest(test_case,target))        