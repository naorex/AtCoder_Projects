# 黒板に書かれた整数がすべて偶数である間、整数を2で割り続ける操作を最大で何回行えるかを計算する。

def max_operations(n, a):
    '''
    x % 2 == 0 は、要素 x が偶数であることを確認します。
    偶数の数を2で割った余りは0になるため、この条件が True であれば x は偶数です。

    for x in a は、リスト a のすべての要素を順番に x に代入していきます。
    ジェネレータ式 x % 2 == 0 for x in a は、リスト a のすべての要素に対して
    x % 2 == 0 が True かを評価する一連のブール値 (True または False) を生成します。

    all() 関数は、ジェネレータ式によって生成されたすべてのブール値が True であるかを確認します。
    すべてが True であれば True を返し、1つでも False があれば False を返します。
    '''
    count = 0
    while all(x % 2 == 0 for x in a):
        a = [x // 2 for x in a]
        count += 1
    return count

# 標準入力からの読み込み
import sys
input = sys.stdin.read  # 一度に全ての入力を読み取る
data = input().split()

n = int(data[0])
a = list(map(int, data[1:]))

print(max_operations(n, a))
