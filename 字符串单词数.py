class Solution:
    def count(self,s):
        res = 0
        for i in range(len(s)):
            if s[i]!= ' 'and (i==0 or s[i-1]==' '):
                res+=1
        return res
if __name__ == '__main__':
    s=Solution()
    n="Hello, my name is john"
    print('字符长度：',len(n))
    print('输入：',n)
    print('输出：',s.count(n))
