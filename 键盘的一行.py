class Solution:
    # 参数words为字符串列表，用于存储待检查的单词
    # 返回字符串列表，包含仅使用同一行字母的单词
    def findWords(self, words):
        res = []  # 初始化返回结果的列表
        s = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]  # 定义键盘的三行字母
        for w in words:  # 遍历给定的单词列表
            for j in range(3):  # 遍历三行字母
                flag = 1  # 初始化标志位，标记是否只使用了同一行的字母
                for i in w:  # 遍历单词中的每个字母
                    if i.lower() not in s[j]:  # 如果字母不在当前行中
                        flag = 0  # 设置标志位为0，表示不是同一行字母
                        break  # 跳出字母循环
                if flag == 1:  # 如果所有字母都在同一行
                    res.append(w)  # 将单词添加到结果列表
                    break  # 跳出行循环，继续下一个单词
        return res  # 返回结果列表
# 主函数
if __name__ == '__main__':
    word = ["Hello", "Alaska", "Dad", "Peace"]  # 定义待检查的单词列表
    s = Solution()  # 创建Solution类的实例
    print("输入为：", word)  # 打印输入的单词
    print("输出为：", s.findWords(word))  # 打印使用同一行字母的单词
