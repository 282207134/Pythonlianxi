#参数length是棋盘长度（不包含起始点）
#参数connections是跳点的集合
#返回值是个整数，代表最小步数
class Solution:
    def modernLudo(self, length, connections):
        ans = [i for i in range(length+1)]
        for i in range(length+1):
            for j in range(1,7):
                if i - j >= 0:
                    ans[i] = min(ans[i], ans[i-j]+1)
            for j in connections:
                if i == j[1]:
                    ans[i] = min(ans[i], ans[j[0]])
        return ans[length]
#SPFA解法
class Solution:
    """
    参数length为棋盘长度
    参数connections为连接位置表
    返回最小次数
    """
    def modernLudo(self, length, connections):
        dist = [1000000000 for i in range(100050)]
        vis  = [0 for i in range(100050)]
        Q  = [0 for i in range(100050)]
        st = 0
        ed = 0
        dist[1] =0
        vis[1] = 1
        Q[ed] = 1;
        ed += 1
        while(st<ed) :
            u = Q[st]
            st += 1
            vis[u] = 0
            for roads in connections :
                if(roads[0] != u):
                    continue
                v = roads[1]
                if(dist[v] > dist[u]):
                    dist[v] = dist[u]
                    if(vis[v] == 0) :
                        vis[v] = 1
                        Q[ed] = v
                        ed += 1
            for i in range(1, 7):
                if (i + u > length):
                    break
                v = i + u
                if(dist[v] > dist[u] + 1) :
                    dist[v] = dist[u] + 1
                    if(vis[v] == 0):
                        vis[v] = 1
                        Q[ed] = v
                        ed += 1
        return dist[length]
if __name__ == '__main__':
    length = 15
    connections = [[2, 8],[6, 9]]
    solution = Solution()
    print(" 棋盘长度为：", length)
    print(" 连接为：", connections)
    print(" 最小需要为:", solution.modernLudo(length, connections))
