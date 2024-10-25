class Solution:
    # 参数arr是输入的待查数组
    # 返回值是两个值的列表，内容没有重复的
    def theTwoNumbers(self, a):
        ans = [0, 0]

        # 第一次遍历，找出所有数字的异或结果，保存在ans[0]
        for i in a:
            ans[0] = ans[0] ^ i

        # 找到ans[0]中第一个为1的位，保存在c中
        c = 1
        while c & ans[0] != c:
            c = c << 1

        # 第二次遍历，根据c将数字分成两组，分别进行异或运算
        for i in a:
            if i & c == c:
                ans[1] = ans[1] ^ i

        # 计算第一个唯一的数字
        ans[0] = ans[0] ^ ans[1]

        return ans


if __name__ == '__main__':
    arr = [1, 2, 5, 1]
    solution = Solution()
    print("数组为：", arr)
    print("两个没有重复的数字是:", solution.theTwoNumbers(arr))
