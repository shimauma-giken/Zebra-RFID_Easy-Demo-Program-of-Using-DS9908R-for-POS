import sys
import os.path
import shutil
import datetime
from zebra import Zebra

# Global Variables 
# printername = 'ZDesigner ZD621R-203dpi ZPL'   # プリンタ名
scanData = ''   # スキャンデータ
zpl = ''        # 印刷スクリプト
zpl1 = '''
^XA
^XZ
'''

purchaseList = []   # 購入品リスト
totalPrice = 0      # 購入合計

# 購入リスト・合計の初期化
def resetData():
    global purchaseList
    global totalPrice
    purchaseList = []
    totalPrice = 0

# 商品詳細表示
def prtAsset(asset):
    print("\n")
    print("商品 ：", asset[0])
    print("詳細 ：", asset[1])
    print("価格 ：", asset[2], "円")
    global purchaseList
    purchaseList.append(asset)
    print ('-' * 30)
    global totalPrice
    totalPrice = totalPrice + asset[2]
    print("合計金額:", totalPrice)

# 簡易マスターデータ
asset01 = ["ボーダー柄スニーカーイン", "Navy, 25-27cm", 200]
asset02 = ["宇治抹茶ラテ", "170g(10杯分)", 390]    # 4550583992545
asset03 = ["キーマカレー", "180g", 350]    # 4550002861308
asset04 = ["タオルハンカチ", "ベージュボーダー", 390] # 303515BEDC3280D82A00737E, 4550583517151
asset05 = ["ハンカチ", "ダークネイビー", 390]    # 303515BEE00C84982A00429B, 4550584128189
asset06 = ["和晒しハンカチ", "オフ白", 390]    # 303515BEDC32825824004393, 4550583517212


# 0. Initial Process 
print ('\n' * 25)
print ('-' * 30)
print ('COPY RIGHT: Shimauma-Giken Software')
print ('Product: DS9908R Payment Demo v0.1')
print ('-' * 30)
print ('')
print ('[注意すべき事項]')
print ('1. プログラム終了時は本画面をXボタンで閉じてください。')
print ('2. キーボード入力を「半角英数」にご設定ください。')
print ('')
print ('-' * 30)
print ("Have Fun with Zebra!!")
print ('\n' * 2)


msgInit = """
アイテムをスキャンしてください。
: 会計の場合は[k + Enter]
: キャンセルの場合は[c + Enter]
\n
"""

msgKaikei = """
会計処理を実行します。
\n
"""

msgCancel = """
会計処理をキャンセルしました。
\n
"""

while True:
        
    print ('-' * 30)
    scanData = input(msgInit)
    # print(scanData, 'をスキャンしました。')

    match scanData:
        case "k" :
            print(msgKaikei)
            print ('-' * 30)
            print("お買い上げ商品一覧")
            print ('-' * 30)
            for item in purchaseList:
                print(item[0], item[1], item[2], "円")
            print ('-' * 30)
            print("お会計合計", totalPrice, "円")
            resetData()
        case "c" :
            print(msgCancel)
            print(msgInit)
            resetData()
        case "4550583992545" :
            prtAsset(asset02)
        case "4550002861308" :
            prtAsset(asset03)
        case "303515BEDC3280D82A00737E" :
            prtAsset(asset04)
        case "303515BEE00C84982A00429B" :
            prtAsset(asset05)
        case "303515BEDC32825824004393" :
            prtAsset(asset06)
        case "4550583517151" :
            prtAsset(asset04)
        case "4550584128189" :
            prtAsset(asset05)
        case "4550583517212" :
            prtAsset(asset06)
        case _:
            print("マスターDBにアイテムが存在しません。")
            zpl = ''

    print ('\n' * 2)

    # レシート印刷をする場合は設定
    # today = datetime.datetime.now()
    # print(today)
    #print ('-' * 30)

    # print( 'GENERATED ZPL: ' + zpl1)
    # print('ACTION: print data has been sent to your printer')
            
    # 1. send zpl to printer via windows driver
    # z = Zebra(printername)
    # z.output(zpl)

