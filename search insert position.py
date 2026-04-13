def searchInsert(self, nums, target):
        l=len(nums)
        for i in range(l):
            if nums[i]>=target:
                return i
        return l
