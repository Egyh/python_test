x = 1
y = 0

try:
    result = x / y

except ZeroDivisionError as e:
    print('ゼロで割り切ることができません。')
    print(e)#pythonの詳細説明を表記
 

#except NameError as e:
    #print('変数が定義されていません')
    #print(e)   
    
    #ｙが定義されていない時に出力される

#else:
    #print(result)
    #print('正常に終了しました')
    
    #例外が発生しなかった時の場合

#finally:
    #print('割り算を終了します')
    
    #最後に必ず実行される