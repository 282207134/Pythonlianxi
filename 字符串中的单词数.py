class Solution:
    # 参数s为字符串
    # 返回整数
    def countSegments(self, s):
        # 初始化计数器res为0
        res = 0
        # 遍历字符串s的每一个字符
        for i in range(len(s)):
            # 如果当前字符不是空格并且（是第一个字符或前一个字符是空格）
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                # 将计数器res加1
                res += 1
        # 返回计数器res的值
        return res

# 主函数
if __name__ == '__main__':
    s = Solution()
    # 初始化字符串n
    n =  "Hello, my name is John"
    # 打印输入的字符串
    print("输入为：", n)
    # 打印字符串中的单词数
    print("输出为：", s.countSegments(n))
