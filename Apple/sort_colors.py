class Solution:
  def sortColors(self, nums):
    max = 2
    count_array = [0]*(max+1)

    for i in nums: # O(n)
        count_array[nums[i]] += 1

    for index in range(1, len(count_array)): # O(max)
        count_array[index] += count_array[index-1]

    output = [0]*len(nums)
    for i, val in enumerate(nums): # O(n)
        output[count_array[val]-1] = val
        count_array[val] -= 1

    nums[:] = list(output)

# Use Count sort for the linear solution

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
