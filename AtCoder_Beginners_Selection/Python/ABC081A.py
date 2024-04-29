# 入力を整数で受けて、文字列型へ
input = str(int(input()))

# inputの文字列を各要素毎にint型へ変更
count = sum(map(int, input))

'''
map(int, input)は、入力された文字列の各文字をintに変換したイテレータを生成します。
例えば、inputが"123"の場合、mapは[1, 2, 3]を生成します。
'''

print(count)
