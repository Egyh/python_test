x_set = {11, 222, 333}

y_list = [11 , 333, 444, 555, 11]
y_set = set(y_list)#リストから集合に変換

print(x_set)
print(y_list)

a_set = {11, 222, 333}

b_list = [11 , 333, 444, 555, 11]
b_set = set(b_list)#リストから集合に変換

result = a_set & b_set #共通の数値のみ
print(result)

#result = a_set - b_set #aにはあってbには存在しない値(差集合)
#result = a_set | b_set #両方の和集合