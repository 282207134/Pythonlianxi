class Solution:
    # 参数s: 字符列表
    # 参数offset: 整数
    # 返回值: 无
    def rotateString(self, s, offset):
        # 如果s的长度大于0，则进行旋转操作
        if len(s) > 0:
            # 计算有效的偏移量，即offset对s的长度取模，避免超出范围的偏移量
            offset = offset % len(s)
        # 通过将s与自身拼接，并截取特定范围的子串，得到旋转后的结果
        temp = (s + s)[len(s) - offset : 2 * len(s) - offset]
        # 将旋转后的结果赋值回原列表s
        for i in range(len(temp)):
            s[i] = temp[i]

# 主函数
if __name__ == '__main__':
    # 定义字符列表s和偏移量offset
    s = ["a","b","c","d","e","f","g"]
    offset = 3
    # 创建Solution类的实例
    solution = Solution()
    # 调用rotateString方法进行旋转操作
    solution.rotateString(s, offset)
    # 输出结果
    print("输入：s =", ["a","b","c","d","e","f","g"], " ", "offset =",offset)
    print("输出：s =", s)
