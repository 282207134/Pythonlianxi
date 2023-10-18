# 文字列の長さ N を入力
N = int(input())
# 文字列 S を入力
S = input()
# アルファベットポイント対応表
alphabet_points = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}
# アルファベットポイントを計算
total_points = sum(alphabet_points[char] for char in S)
# 結果を出力
print(total_points)