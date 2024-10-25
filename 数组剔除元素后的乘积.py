class Solution:
    #参数A: 整数数组A
    #返回值: 整数数组B
    def productExcludeItself(self, A):
        length ,B  = len(A) ,[]
        f = [ 0 for i in range(length + 1)]
        f[ length ] = 1
        for i in range(length - 1 , 0 , -1):
            f[ i ] = f[ i + 1 ] * A[ i ]
        tmp = 1
        for i in range(length):
            B.append(tmp * f[ i + 1 ])
            tmp *= A[ i ]
        return B
#主函数
if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 3, 4]
    B = solution.productExcludeItself(A)
    print("输入：", A)
    print("输出：", B)