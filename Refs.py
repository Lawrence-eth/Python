#字典資料型態由 鍵/值 組成
#e.g. 英文字典 英文單字為鍵，翻譯為值 （兩者為一對一的關係）
#key:value
#value可以是數值、布林、串列等等，擷取字典時以鍵取值

#字典特性
#資料可變動
#鍵值對
#儲存非重複項目（鍵無法重複，值反之）
#有順序

#建立空字典
my_dict = {}
print(my_dict)

#e.g.
stock = {"Laptop":"Macbook Air", "Headphone":"Pixel Buds Pro"}
print(stock["Headphone"])
#Pixel Buds Pro

stock = {"Laptop":"Macbook Air", "Headphone":"Pixel Buds Pro"}
stock["Laptop"] = 'MacBook Pro'
print(stock["Laptop"])
#MacBook Pro