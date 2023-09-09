phone1 = {
    'brand':'samsung',
    'colour':'Black',
    'model':'Galaxy S23 Ultra',
    'storage':'256 GB'
}
phone2 = {
    'brand':'google',
    'colour':'Green',
    'model':'Pixel 8',
    'storage':'128 GB'
}
phone3 = {
    'brand':'apple',
    'colour':'White',
    'model':'iPhone X',
    'storage':'64 GB'
}
brand = input(f"Please enter the name of the brand you want to look up.")
stock = [phone1, phone2, phone3]
if brand in str(stock):
    for phone in stock:
        if phone['brand'] == brand:
            print(f"There's {phone['colour']} {phone['model']} with {phone['storage']} of storage in stock now.")
else:
    print(f"Out of Stock.")