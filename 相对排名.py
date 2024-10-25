class Solution:
    # 参数 nums 为整数列表
    # 返回一个包含排名或奖牌的列表
    def findRelativeRanks(self, nums):
        # 创建一个字典，用于存储每个分数及其对应的索引
        score = {}
        for i in range(len(nums)):  # 遍历 nums 列表的每个元素
            score[nums[i]] = i  # 将当前元素作为键，索引作为值存入字典
        #score={0,1,2,3,4,5}
        # 对 nums 列表进行降序排序，得到 sortedScore
        sortedScore = sorted(nums, reverse=True)

        # 初始化一个长度与 nums 相同的列表 answer，用于存储最终结果
        answer = [0] * len(nums)

        # 遍历排序后的分数列表
        for i in range(len(sortedScore)):
            # 将当前排名（索引 + 1）转换为字符串
            res = str(i + 1)
            # 判断当前排名，分配对应的奖牌名称
            if i == 0:
                res = 'Gold Medal'  # 第一名分配金牌
            elif i == 1:
                res = 'Silver Medal'  # 第二名分配银牌
            elif i == 2:
                res = 'Bronze Medal'  # 第三名分配铜牌
            # 根据原始索引将排名或奖牌赋值给 answer 列表
            answer[score[sortedScore[i]]] = res

        # 返回最终的结果列表
        return answer


# 主函数
if __name__ == '__main__':
    num = [5, 4, 3, 2, 1]  # 定义输入的分数列表
    s = Solution()  # 创建 Solution 类的实例
    print("输入为：", num)  # 打印输入
    print("输出为：", s.findRelativeRanks(num))  # 调用 findRelativeRanks 方法并打印输出
