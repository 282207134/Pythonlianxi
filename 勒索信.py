class Solution:
    """    参数ransomNote为字符串
        参数magazine为字符串
            返回布尔类型  """
    def canConstruct(self, ransomNote, magazine):
        arr = [0] * 26
        for c in magazine:
            arr[ord(c) - ord('a')] += 1
        for c in ransomNote:
            arr[ord(c) - ord('a')] -= 1
            if arr[ord(c) - ord('a')] < 0:
                return False
        return True