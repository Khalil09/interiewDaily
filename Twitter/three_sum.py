class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort() # O(nlog(n))

        for i in range(len(nums) - 2):
            if nums[i] > 0: # If i > 0 so the l and r necessarily will be positive
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, ((len(nums)-1) - i)

            while(l < r):
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while(l < r and nums[l] == nums[l+1]):
                        l += 1
                    while(l < r and nums[r] == nums[r-1]):
                        r -= 1

                    r -= 1
                    l += 1
                else:
                    if nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
                    else:
                        l += 1

        return result

# Test Program
# nums = [1, -2, 1, 0, 5]
nums = [1, -2, 1, 1, -3, 1, 0, 5]
#   i     l  r
# [-2, 0, 1, 1, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
