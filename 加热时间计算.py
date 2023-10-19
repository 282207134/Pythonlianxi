def microwave_heating_time(N, S):
    allowed_foods = "cbpho"  # 電子レンジで加熱できる食品を示す文字列
    time = 0
    for food in S:
        if food not in allowed_foods:
            break  # 電子レンジで加熱できない食品が含まれた場合、中止
        if food == 'c':
            time += 4 * 60  # カレーは4分
        elif food == 'b':
            time += 3 * 60  # ビーフシチューは3分
        elif food == 'p':
            time += 3 * 60  # パスタソースは3分
        elif food == 'h':
            time += 1 * 60 + 30  # ハンバーグは1分30秒
        elif food == 'o':
            time += 50  # オムレツは50秒
    return time
# 入力を受け取る
N = int(input())
S = input()
# 出力
time = microwave_heating_time(N, S)
print(time)
