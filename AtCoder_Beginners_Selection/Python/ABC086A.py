# 整数を入力
a,b = map(int, input().split())

# 2で割り切れるかどうかで偶数奇数を判定
if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")
