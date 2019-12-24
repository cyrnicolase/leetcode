class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.sum = [0] * len(self.nums)
        self.init()

    def sumRange(self, i, j):
        if 0 == i:
            return self.sum[j]
        
        return self.sum[j] - self.sum[i - 1]

    def init(self):
        add = 0
        count = len(self.nums)
        for i in range(count):
            add += self.nums[i]
            self.sum[i] = add


nums= [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
            