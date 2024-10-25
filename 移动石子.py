#参数arr是一个列表
#返回值为整数，为最小移动次数
class Solution:
    def movingStones(self, arr):
        arr = sorted(arr)
        even = 0
        odd = 0
        for i in range(0,len(arr)):
            odd += abs(arr[i]-(2*i+1))
            even += abs(arr[i] - (2*i+2))
        if odd < even:
            return odd
        return even
if __name__ == '__main__':
    arr = [1, 6, 7, 8, 9]
    solution = Solution()
    print(" 数组是：", arr)
    print(" 最小移动数是:", solution.movingStones(arr))
