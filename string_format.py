x = 'yamada'
y = 'taro'

result = f'{x + y}san'
print(result)

x = 123
result = f'No: {x:010}'#10桁になるように表記
print(result)

x = 9000000
result = f'{x:,}yen'#金額用のカンマ
print(result)

x = 0.123
result = f'{x:.9f}'
print(result)