# 入力を受け取る
import sys
input = sys.stdin.read  # 一度に全ての入力を読み取る
data = input().split()
A = int(data[0])  # 500円玉の枚数
B = int(data[1])  # 100円玉の枚数
C = int(data[2])  # 50円玉の枚数
X = int(data[3])  # 合計金額


# 方法の数をカウントする変数
count = 0

# 500円玉の枚数を全て試す
for a in range(A + 1):
    # 100円玉の枚数を全て試す
    for b in range(B + 1):
        # 50円玉の枚数を全て試す
        for c in range(C + 1):
            # 合計金額を計算する
            total = 500 * a + 100 * b + 50 * c
            # 合計金額がX円に一致する場合、カウントを増やす
            if total == X:
                count += 1

# 結果を出力する
print(count)
