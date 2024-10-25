class Solution:
    # 参数nums1为整数数组
    # 参数nums2为整数数组
    # 返回整数数组
    def nextGreaterElement(self, nums1, nums2):
        # 创建一个字典用于存储每个数字的下一个更大元素
        answer = {}
        # 使用一个栈来帮助找到下一个更大元素
        stack = []
        # 遍历nums2中的每个元素
        for x in nums2:
            # 当栈不为空且栈顶元素小于当前元素时，更新栈顶元素的下一个更大元素
            while stack and stack[-1] < x:
                answer[stack[-1]] = x
                del stack[-1]
            # 将当前元素压入栈中
            stack.append(x)
        # 对于栈中剩下的元素，它们没有下一个更大元素，将其对应值设为-1
        for x in stack:
            answer[x] = -1
        # 返回nums1中每个元素在answer字典中对应的值
        return [answer[x] for x in nums1]

# 主函数
if __name__ == '__main__':
    s = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print("输入1为：", nums1)
    print("输入2为：", nums2)
    print("输出为 ：", s.nextGreaterElement(nums1, nums2))
