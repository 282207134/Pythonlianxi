def calculate_bowling_score(frames):
    total_score = 0
    frame = 0
    for i in range(len(frames)):
        if frame == 10:
            break
        if frames[i][0] == 10:  # ストライク
            total_score += 10
            if i + 1 < len(frames):
                total_score += frames[i + 1][0]  # 次の1投目の得点
                if frames[i + 1][0] == 10:  # 次のフレームもストライク
                    if i + 2 < len(frames):
                        total_score += frames[i + 2][0]  # 次の2投目の得点
                    else:
                        break
                else:
                    total_score += frames[i + 1][1]  # 次の2投目の得点
        else:
            frame_score = sum(frames[i])
            total_score += frame_score
            if frame_score == 10:  # スペア
                if i + 1 < len(frames):
                    total_score += frames[i + 1][0]  # 次の1投目の得点
        frame += 1
    return total_score
frames=[]
a=int(input())
for i in range(a):
    x,y=input().split()
    b=(int(x),int(y))
    frames.append(b)
final_score = calculate_bowling_score(frames)
# 結果を出力
print(final_score)

