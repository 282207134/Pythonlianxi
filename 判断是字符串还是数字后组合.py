# 读取Q、C、N的值
Q, C, N = input().split()
Q = int(Q)
N = int(N)
result_C = C
result_N = N
# 逐行处理查询
for i in range(Q):
    Ai = input()
    if Ai.isnumeric():  # 如果Ai是整数
        Ai = int(Ai)
        result_N += Ai
    else:  # 如果Ai是字符串
        result_C += Ai
# 输出最终结果
print(result_C)
print(result_N)