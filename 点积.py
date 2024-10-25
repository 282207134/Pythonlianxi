class Solution:
    # 参数A和B是输入列表
    # 返回值是个整数，是点积
    def dotProduct(self, A, B):
        # 如果A或B为空列表，或者A和B的长度不相等，返回-1
        if len(A) == 0 or len(B) == 0 or len(A) != len(B):
            return -1
        ans = 0
        # 遍历A和B的每一个元素，计算点积
        for i in range(len(A)):
            ans += A[i] * B[i]
        return ans
if __name__ == '__main__':
    A = [1, 1, 1]
    B = [2, 2, 2]
    solution = Solution()
    print("A与B分别为：", A, B)
    print("点积为：", solution.dotProduct(A, B))
