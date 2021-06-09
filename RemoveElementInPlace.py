#Program submitted to leetcode to solve problem of deleting values from a
#list in place, making no copies of arrays for iteration

nums = [1,2,2,3,4,6,2,8,9,2]
val = 2
toDelete = []
class Solution(object):
    def removeElement(nums, val):
        for i, value in enumerate(nums):
            if val == value:
                toDelete.append(i)
        count = 0
        for i in range(len(toDelete)):
            del nums[toDelete[i]-count]
            count += 1
        return len(nums)
    #Driver code to test method
    result = removeElement(nums, val)
    print(result)
    print(nums)
