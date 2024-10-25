class Solution:
    # 参数 nums: 整数数组
    # 参数 target: 要查找的目标数字
    # 返回值：目标数字的第一个位置，从0开始
    def binarySearch(self, nums, target):
        # 调用 search 方法，传递数组，起始索引0，结束索引len(nums) - 1，以及目标值
        return self.search(nums, 0, len(nums) - 1, target)

    def search(self, nums, start, end, target):
        # 如果起始索引大于结束索引，表示查找范围无效，返回 -1
        if start > end:
            return -1
        # 计算中间索引
        mid = (start + end) // 2
        # 如果中间值大于目标值，在左半部分查找
        if nums[mid] > target:
            return self.search(nums, start, mid - 1, target)
        # 如果中间值等于目标值，返回中间索引
        if nums[mid] == target:
            return mid
        # 如果中间值小于目标值，在右半部分查找
        if nums[mid] < target:
            return self.search(nums, mid + 1, end, target)

# 主函数
if __name__ == '__main__':
    # 创建 Solution 类的一个实例
    my_solution = Solution()
    # 定义要查找的数组
    nums = [1, 2, 3, 4, 5, 6]
    # 定义目标值
    target = 3
    # 调用 binarySearch 方法查找目标值的索引
    targetIndex = my_solution.binarySearch(nums, target)
    # 打印输入数组和目标值
    print("输入：nums =", nums, " ", "target =", target)
    # 打印查找结果
    print("输出：", targetIndex)
