#参数array是输入列表
#参数target是目标值
#返回值是整数
class Solution:
    def closestTargetValue(self, target, array):
        n = len(array)
        if n < 2:
            return -1
        array.sort()
        diff = 0x7fffffff
        left = 0
        right = n - 1
        while left < right:
            if array[left] + array[right] > target:
                right -= 1
            else:
                diff = min(diff, target - array[left] - array[right])
                left += 1
        if diff == 0x7fffffff:
            return -1
        else:
            return target - diff
if __name__ == '__main__':
    array = [1,3,5,11,7]
    target = 15
    solution = Solution()
    print(" 输入数组为：", array,"目标值为：", target)
    print(" 最近可以得到值为:", solution.closestTargetValue(target, array))
