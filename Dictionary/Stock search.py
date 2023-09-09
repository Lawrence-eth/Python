phone1 = {
    'brand':'google',
    'storage':'256 GB',
    'model':'Pixel 7 Pro',
    'colour':'Green'
}
phone2 = {
    'brand':'samsung',
    'storage':'512 GB',
    'model':'Galaxy S23 Ultra',
    'colour':'Black'
}
phone3 = {
    'brand':'apple',
    'storage':'128 GB',
    'model':'iPhone X',
    'colour':'White'
}
stock = [phone1, phone2, phone3]
sbrand = input(f"Please enter the brand of the phone you want to look up").lower()
if sbrand in str(stock): # 如果查詢的品牌在 stock 清單中
    for phone in stock: # 針對 stock 中的每支手機
        #(這邊是將stock中的每個phone指派為phone
        #接著下面檢查哪一個phone符合查詢的品牌將其設為phone，方便於最終print指派
        # 因為不知道是哪一隻phone符合所以需要用指派的)
        if phone['brand'] == sbrand: #如果stock中的手機品牌＝查詢品牌
            print(f"There's a {phone['colour']} {phone['model']} with {phone['storage']} of storage in stock now ")
else:
    print("Out of stock.")
