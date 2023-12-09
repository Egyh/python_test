a = 1
b = 5
print (a + b)

print("hello world")
#comment

x = 'abcde'
print(x)

x = ['a','b','C','d','e']
result = x[2]
print(result)

x = ['a','b','C','d','e']
x[1] = 'B'
print(x)

x = ['a', 'b']
y = ['A', 'B']

x.extend(y)#xにyを結合
print(x)

x = ['a','b','C','d','e']
x_len = len(x)#リストの長さを表記
print(x_len)

x = { 'リンゴ': 150, 'バナナ': 300, 'オレンジ': 100}
result = x['バナナ']#バナナの値段を取得
print(result)

x == 9
if x == 10:
    print('This is 10')
elif x == 9:
    print('This is not 10')
else:
    print('This is neither 10 or 9')
    
for x in range(10):#1~9までを表記
    print(x)
   
x_list = [5,10,20,-5]
for x in x_list:
    x_twice = x * 2 #リストの要素を2倍
    print(x_twice) 

x = { 'リンゴ': 150, 'バナナ': 300, 'オレンジ': 100}

for name, price in x.items():
    print(name,price)
    
def average_calc(x, y):
    print('２つの数の平均を計算する処理です')
    avg = ( x + y) / 2
    return avg

result = average_calc(7,19)
print(result)

class BodyCondition:
    def __init__(self,arg_weight,arg_height):#イニシャライザー
        self.weight = arg_weight #インスタンス変数
        self.height = arg_height #インスタンス変数
    
    def bmi_calc(self):
        m_height = self.height / 100
        bmi = self.weight / m_height / m_height
        print(bmi)
        
bc = BodyCondition(55,150)#bcにBodyConditionクラスを代入
bc.bmi_calc()       
        